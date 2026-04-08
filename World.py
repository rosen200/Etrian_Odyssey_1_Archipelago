import zipfile
import os
import yaml

import Utils

import settings
import typing

from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World
from .Constant import *

from .Options import EtrianOdysseyOptions
from .data.InventoryItemData import *
from .data.TreasureData import *
from .Items import *
from .Locations import *
from .data.RegionData import EO1Regions, STRATUM_5
from . import Items, Locations, Regions, Rules, WebWorld
from base64 import b64encode
from worlds.Files import APPlayerContainer
from .Rules import *
#from rule_builder.cached_world import CachedRuleBuilderWorld


#from Utils import visualize_regions

class EtrianOdysseySettings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the Etrian Odyssey ROM file."""
        description = "Etrian Odyssey ROM File"
        copy_to = "ETRIAN_ODYSSEY_1.nds"
        md5 = "52c259854a469213d1858d7d255519fc"

    rom_file: RomFile = RomFile(RomFile.copy_to)

class EO1Container(APPlayerContainer):
    game = GAME_NAME
    patch_file_ending = ".apeo1"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        if "data" in kwargs:
            self.data = kwargs["data"]
            del kwargs["data"]

        super().__init__(*args, **kwargs)

    def write_contents(self, opened_zipfile: zipfile.ZipFile) -> None:
        super().write_contents(opened_zipfile)
        opened_zipfile.writestr("patch", b64encode(bytes(yaml.safe_dump(self.data, sort_keys=False), "utf-8")))

class EtrianOdysseyWorld(World):
#class EtrianOdysseyWorld(CachedRuleBuilderWorld):
    """Etrian Odyssey is a dungeon crawler RPG first developed by Atlus in 2007 on the Nintendo DS."""
    game = GAME_NAME
    web = WebWorld.EtrianOdysseyWebWorld()

    options_dataclass = EtrianOdysseyOptions
    options: EtrianOdysseyOptions
    settings: typing.ClassVar[EtrianOdysseySettings]
    topology_present = True
    #explicit_indirect_conditions = False

    location_name_to_id = ALL_LOCATIONS_ID_BY_NAME
    item_name_to_id = ITEMS_ID_BY_NAME
    item_name_groups = {
        ItemGroupNames.MONEY: {money_data.name for money_data in ALL_MONEY_ITEMS},
        ItemGroupNames.PROGRESSIVE_LEVEL_CAP: {level_cap_data.name for level_cap_data in ALL_PROGRESSIVE_LEVEL_CAP},
        ItemGroupNames.PROGRESSIVE_FLOOR_LIMIT: {floor_limit_data.name for floor_limit_data in ALL_PROGRESSIVE_FLOOR_LIMIT},
        ItemGroupNames.CLASS: {class_data.name for class_data in ALL_CLASS_DATA},
        ItemGroupNames.SKILL: {skill_data.ap_item_name for skill_data in ALL_SKILLS_ITEMS},
        ItemGroupNames.KEY_ITEM: {key_item.name for key_item in KEY_ITEM_DATA},
        ItemGroupNames.CONSUMABLE: {consumable_data.name for consumable_data in CONSUMABLE_DATA},
        #ItemGroupNames.QUEST_ITEM: {quest_item.name for quest_item in QUEST_ITEM_DATA},
        # Consider splitting this into different groups.
        ItemGroupNames.EQUIPMENT: {equipment.name for equipment in ALL_EQUIPMENT_DATA}
    }
    item_mapping = {
        **{skill_data.ap_item_name:ItemGroupNames.SKILL for skill_data in ALL_SKILLS_ITEMS},
        **{class_data.name:ItemGroupNames.CLASS for class_data in ALL_CLASS_DATA},
        **{level_cap_data.name:ItemGroupNames.PROGRESSIVE_LEVEL_CAP for level_cap_data in ALL_PROGRESSIVE_LEVEL_CAP},
        **{floor_limit_data.name:ItemGroupNames.PROGRESSIVE_FLOOR_LIMIT for floor_limit_data in ALL_PROGRESSIVE_FLOOR_LIMIT},
        **{key_item.name:ItemGroupNames.KEY_ITEM for key_item in KEY_ITEM_DATA},
        **{event:ItemGroupNames.EVENT for event in EVENT_BY_NAME}
    }

    origin_region_name = EO1Regions.ETRIA

    starting_classes: list[str]
    starting_skills: list[SkillItem]
    initial_floor_limit: int
    initial_level_cap: int

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.initial_floor_limit = MAX_FLOOR
        self.initial_level_cap = MAX_LEVEL
        self.starting_classes = []
        self.starting_skills = []

    def collect(self, state: "CollectionState", item: "Item") -> bool:
        change = super().collect(state, item)
        if change:
            state.etrianodyssey_logic_data[self.player].collect(state, item)
        return change

    def remove(self, state: "CollectionState", item: "Item") -> bool:
        change = super().remove(state, item)
        if change:
            state.etrianodyssey_logic_data[self.player].remove(state, item)
        return change

    def generate_early(self) -> None:
        starting_classes = get_starting_classes(self)
        self.starting_classes = [class_data.name for class_data in starting_classes]

        for class_data in starting_classes:
            self.multiworld.push_precollected(Items.create_item_from_class_data(class_data, self.player))

        self.starting_skills = get_starting_skill_items(self)
        for skill_item in self.starting_skills:
            self.multiworld.push_precollected(create_item_from_skill_item(skill_item, self.player))

        self.initial_floor_limit = self.options.get_effective_initial_floor_limit()
        self.initial_level_cap = self.options.get_effective_initial_level_cap()

    def create_regions(self) -> None:
        Regions.create_and_connect_regions(self)
        Locations.create_all_locations(self)

    def set_rules(self) -> None:
        Rules.set_all_rules(self)

    def create_items(self) -> None:
        self.multiworld.itempool += Items.create_all_items(self)
        create_events(self)

    def create_item(self, name: str) -> Items.EtrianOdysseyItem:
        return Items.create_item_from_name(self, name)

    def get_filler_item_name(self) -> str:
        return Items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = self.options.as_dict(
            "goal"
        )
        return slot_data

    def generate_output(self, output_directory: str) -> None:
        multiworld = self.multiworld
        player = self.player
        output_data = {
            "Version": GAME_VERSION,
            "Seed": multiworld.seed_name,
            "Slot": player,
            "Name": self.player_name,
            "InitialValues": {},
            "TreasureBoxes": []
        }

        if self.options.level_cap_mode != 0:
            output_data["InitialValues"]["level_cap"] = self.initial_level_cap
        if self.options.floor_limit_mode != 0:
            output_data["InitialValues"]["floor_limit"] = self.initial_floor_limit

        output_data["ShopUnlockMaterialCostDivider"] = self.options.shop_unlock_material_cost_divider.value

        output_data["InitialValues"]["experience_modifier"] = int(self.options.experience_modifier)

        output_data["InitialValues"]["landsknecht_unlocked"] = EO1Class.LANDSKNECHT in self.starting_classes
        output_data["InitialValues"]["survivalist_unlocked"] = EO1Class.SURVIVALIST in self.starting_classes
        output_data["InitialValues"]["protector_unlocked"] = EO1Class.PROTECTOR in self.starting_classes
        output_data["InitialValues"]["dark_hunter_unlocked"] = EO1Class.DARK_HUNTER in self.starting_classes
        output_data["InitialValues"]["medic_unlocked"] = EO1Class.MEDIC in self.starting_classes
        output_data["InitialValues"]["alchemist_unlocked"] = EO1Class.ALCHEMIST in self.starting_classes
        output_data["InitialValues"]["troubadour_unlocked"] = EO1Class.TROUBADOUR in self.starting_classes
        output_data["InitialValues"]["ronin_unlocked"] = EO1Class.RONIN in self.starting_classes
        output_data["InitialValues"]["hexer_unlocked"] = EO1Class.HEXER in self.starting_classes

        # TODO (once implemented) export initial skills unlock.
        # Handle Starting Skills.
        skill_values: list[int] = []
        for index in range(9):
            skill_values.append(0)

        cumulative_skill_items: list[SkillItem] = []
        for skill_item in self.starting_skills:
            skill_values = apply_skill_item_to_values(skill_item, skill_values, cumulative_skill_items)
            cumulative_skill_items.append(skill_item)

        for class_data in ALL_CLASS_DATA:
            output_data["InitialValues"][f"{class_data.name.lower().replace(' ', '_')}_skills"] = skill_values[class_data.class_id]

        # Handle location item patching.
        for location in multiworld.get_locations(player):
            if location.name in EVENT_BY_NAME:
                continue

            location_id = ALL_LOCATIONS_ID_BY_NAME[location.name]
            location_type = ALL_LOCATIONS_BY_ID[location_id].location_type
            if location_type == EtrianOdysseyLocationType.TREASURE_BOX:
                treasure_data = ALL_TREASURE_BY_LOCATION_ID[location_id]
                treasure_type = 0
                treasure_value = 0
                if location.item.player != player:
                    treasure_type = 4
                    treasure_value = 0
                else:
                    item_id = ITEMS_ID_BY_NAME[location.item.name]
                    item_type = ALL_ITEMS_BY_ID[item_id].item_type
                    if item_type == EtrianOdysseyItemType.MONEY:
                        treasure_type = 2
                        treasure_value = ALL_MONEY_BY_ID[item_id].amount
                    elif item_type == EtrianOdysseyItemType.INVENTORY:
                        treasure_type = 3
                        treasure_value = ITEM_PER_AP_ITEM_ID[item_id].item_id
                    #elif item_type == EtrianOdysseyItemType.PROGRESSIVE_FLOOR_LIMIT:
                    #    treasure_type = 5
                    #    treasure_value = ALL_PROGRESSIVE_FLOOR_BY_ITEM_ID[item_id].floor_amount
                    #elif item_type == EtrianOdysseyItemType.PROGRESSIVE_LEVEL_CAP:
                    #    treasure_type = 6
                    #    treasure_value = ALL_PROGRESSIVE_LEVEL_CAP_BY_ITEM_ID[item_id].level_amount
                    #elif item_type == EtrianOdysseyItemType.CLASS:
                    #    treasure_type = 7
                    #    treasure_value = ALL_CLASS_BY_ITEM_ID[item_id].class_id
                    else:
                        treasure_type = 8
                        treasure_value = 0


                def generate_treasure_box_patch_data(floor: int, chest_id: int, type: int, value: int) -> dict[str, int]:
                    return {
                        "floor": floor,
                        "treasure_id": chest_id,
                        "treasure_type": type,
                        "treasure_value": value
                    }

                output_data["TreasureBoxes"].append(generate_treasure_box_patch_data(treasure_data.floor_number - 1, treasure_data.chest_id, treasure_type, treasure_value))

        apeo1 = EO1Container(
            path=os.path.join(
                output_directory, f"{multiworld.get_out_file_name_base(player)}{EO1Container.patch_file_ending}"
            ),
            player = player,
            player_name=self.player_name,
            data=output_data
        )
        apeo1.write()

        # Uncomment to print region diagram (and validate region accessibility).
        #self.output_region_diagram()

    def output_region_diagram(self):
        from Utils import visualize_regions
        state = self.multiworld.get_all_state(False)
        state.update_reachable_regions(self.player)
        regions = [region.name for region in state.reachable_regions[self.player]]
        #for region in STRATUM_5:
            #if region not in regions:
                #raise Exception(f"Region {region} is never reachable")
        visualize_regions(self.get_region("Etria"), "etrian_odyssey.puml", show_entrance_names=True,
                          regions_to_highlight=state.reachable_regions[self.player])
