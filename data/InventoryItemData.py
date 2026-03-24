from typing import TYPE_CHECKING, NamedTuple, Optional
from BaseClasses import ItemClassification
from dataclasses import dataclass
from enum import IntEnum

class EO1ItemType(IntEnum):
    Consumable = 0
    Key = 1
    Equipment = 2
    Quest = 3

class EO1EquipmentType(IntEnum):
    Unknown = 0x00
    Sword = 0x01
    Staff = 0x02
    Axe = 0x03
    Katana = 0x04
    Bow = 0x05
    Whip = 0x06
    Armor = 0x08
    Shield = 0x09
    Headgear = 0x0A
    Gloves = 0x0B
    Boots = 0x0C
    Accessory = 0x0D

@dataclass
class EO1ItemData:
    """
    This class represents the data for an item in Etrian Odyssey.
TODO REVIEW
    """

    type: EO1ItemType
    item_id: int
    name: str
    ap_item_id: int
    classification: ItemClassification
    weight: int

    def __init__(self, item_type: EO1ItemType, item_id: int, name: str, ap_item_id: int, classification: ItemClassification, weight: int = 0):
        self.type = item_type
        self.item_id = item_id
        self.name = name
        self.ap_item_id = ap_item_id
        self.classification = classification
        self.weight = weight

@dataclass
class EO1KeyItem(EO1ItemData):
    associated_flag: int

    def __init__(self, item_id: int, name: str, ap_item_id: int, associated_flag: int):
        super().__init__(EO1ItemType.Key, item_id, name, ap_item_id, ItemClassification.progression)
        self.associated_flag = associated_flag

@dataclass
class EO1EquipmentData(EO1ItemData):
    equipment_type: EO1EquipmentType

    def __init__(self, item_type: EO1ItemType, item_id: int, name: str, ap_item_id: int, equipment_type: EO1EquipmentType):
        super().__init__(item_type, item_id, name, ap_item_id, ItemClassification.filler | ItemClassification.useful)
        self.equipment_type = equipment_type

class EO1ItemNames:
    #JADE_ORE = "Jade Ore"
    MEDICA = "Medica"
    MEDICA_II = "Medica II"
    MEDICA_III = "Medica III"
    MEDICA_IV = "Medica IV"
    MEDICA_V = "Medica V"
    AMRITA = "Amrita"
    AMRITA_II = "Amrita II"
    HAMAO = "Hamao"
    HAMAOPRIME = "Hamaoprime"
    SOMA = "Soma"
    SOMAPRIME = "Somaprime"
    NECTAR = "Nectar"
    NECTAR_II = "Nectar II"
    NECTAR_III = "Nectar III"
    THERIACA_A = "Theriaca A"
    THERIACA_B = "Theriaca B"
    AXCELA = "Axcela"
    AXCELA_II = "Axcela II"
    AXCELA_III = "Axcela III"
    BRAVANT = "Bravant"
    BRAVANT_II = "Bravant II"
    STONARD = "Stonard"
    STONARD_II = "Stonard II"
    FIRE_MIST = "Fire Mist"
    ICE_MIST = "Ice Mist"
    VOLT_MIST = "Volt Mist"
    ALL_MIST = "All Mist"
    BLAZE_OIL = "Blaze Oil"
    FREEZE_OIL = "Freeze Oil"
    SHOCK_OIL = "Shock Oil"
    WARD_CHIME = "Ward Chime"
    GOLD_CHIME = "Gold Chime"
    #DUMMY = "Dummy"
    MAGNET = "Magnet"
    #MAP_EVENT = "Map Event"
    #HOLY_WATER = "Holy Water"
    #WATER = "Water"
    #BOTTLE = "Bottle"
    #JUNK_BOX = "Junk Box"
    #JUNK_BOX = "Junk Box"
    #LOCKET = "Locket"
    #PLANT_SEED = "Plant Seed"
    #GOLD_STONE = "Gold Stone"
    #GOLD_STONE = "Gold Stone"
    #MOON_STONE = "Moon Stone"
    #GOUDA = "Gouda"
    #ODD_POWDER = "Odd Powder"
    #LUCKY_COIN = "Lucky Coin"
    #RUST_SWORD = "Rust Sword"
    #BROKEN_AXE = "Broken Axe"
    #OLD_WAND = "Old Wand"
    #PANACEA = "Panacea"
    #RARE_BLOOM = "Rare Bloom"
    #GOLD_SEED = "Gold Seed"
    #VOX_STONE = "Vox Stone"
    CLEAR_KEY = "Clear Key"
    VIOLET_KEY = "Violet Key"
    #DRAGON_EGG = "Dragon Egg"
    #CARD_KEY = "Card Key"
    #HOLY_GRAIL = "Holy Grail"
    #COPPER_TOP = "Copper Top"
    #SHINY_DISC = "Shiny Disc"
    #SOFT_GLASS = "Soft Glass"
    #TOKEN = "Token"
    #CLAM_TOOL = "Clam Tool"
    #MAGIC_DOWN = "Magic Down"
    #MAGIC_DOWN = "Magic Down"
    #MAGIC_DOWN = "Magic Down"
    #DIAMOND = "Diamond"
    #BLACK_GEM = "Black Gem"
    #SHINY_GEM = "Shiny Gem"
    #OLD_SCROLL = "Old Scroll"
    #HEX_BELL = "Hex Bell"
    #MAP = "Map"
    #RADHA_NOTE = "Radha Note"
    WARP_WIRE = "Warp Wire"
    #TOUGH_FANG = "Tough Fang"
    #TOUGH_WING = "Tough Wing"
    #FROZEN_ARM = "Frozen Arm"
    #ANKH_A = "Ankh A"
    #ANKH_B = "Ankh B"
    #ANKH_C = "Ankh C"
    #ANKH_D = "Ankh D"
    #ANKH_E = "Ankh E"
    #ANKH_MOTOR = "Ankh Motor"
    #BANDANNA = "Bandanna"
    #PEARL = "Pearl"
    #RARE_MEAT = "Rare Meat"

class EO1EquipmentNames:
    KNIFE = "Knife"
    SCRAMASAX = "Scramasax"
    DAGGER = "Dagger"
    SHORTSWORD = "Shortsword"
    BOAR_SPEAR = "Boar Spear"
    BROADSWORD = "Broadsword"
    RAPIER = "Rapier"
    VIKING = "Viking"
    SHAMSHIR = "Shamshir"
    CLAYMORE = "Claymore"
    EXECUTOR = "Executor"
    KATZBALGER = "Katzbalger"
    STEELSWORD = "Steelsword"
    EPEE = "Epee"
    LAST_ESTOC = "Last Estoc"
    PATTISA = "Pattisa"
    FLAMBERGE = "Flamberge"
    DUERGAR = "Duergar"
    SHINRYUU = "Shinryuu"
    BONE_AXE = "Bone Axe"
    HAND_AXE = "Hand Axe"
    CELTIS = "Celtis"
    BROADAXE = "Broadaxe"
    BATTLE_AXE = "Battle Axe"
    BILIOMG = "Biliomg"
    TABAR = "Tabar"
    GREAT_AXE = "Great Axe"
    BARDICHE = "Bardiche"
    HALBERD = "Halberd"
    WAND = "Wand"
    BREAKER = "Breaker"
    LABYRIS = "Labyris"
    FRANCISCA = "Francisca"
    BHUJ = "Bhuj"
    FASCES_AXE = "Fasces Axe"
    FLAME_AXE = "Flame Axe"
    METEOR_AXE = "Meteor Axe"
    HATCHET = "Hatchet"
    STAFF = "Staff"
    BONE_STAFF = "Bone Staff"
    BONE_MACE = "Bone Mace"
    DOWN_STAFF = "Down Staff"
    BONE_FLAIL = "Bone Flail"
    GEM_STAFF = "Gem Staff"
    WAR_MACE = "War Mace"
    LUCK_STAFF = "Luck Staff"
    GODENDAG = "Godendag"
    MYSTIC_ROD = "Mystic Rod"
    WARHAMMER = "Warhammer"
    ARCANA_ROD = "Arcana Rod"
    SAGE_WAND = "Sage Wand"
    WAKIZASHI = "Wakizashi"
    UCHIGATANA = "Uchigatana"
    OHDACHI = "Ohdachi"
    KOGARASU = "Kogarasu"
    SHIDA = "Shida"
    ZANMATOU = "Zanmatou"
    KUZUNOSADA = "Kuzunosada"
    HACHI = "Hachi"
    HISAMEMARU = "Hisamemaru"
    MASAMUNE = "Masamune"
    WOOD_BOW = "Wood Bow"
    ENAMEL_BOW = "Enamel Bow"
    SHORT_BOW = "Short Bow"
    BEAST_BOW = "Beast Bow"
    HARD_SLING = "Hard Sling"
    LONG_BOW = "Long Bow"
    HINDI = "Hindi"
    SELF_BOW = "Self Bow"
    HUNTER_BOW = "Hunter Bow"
    FIN_BOW = "Fin Bow"
    VINE_BOW = "Vine Bow"
    HEAVEN_BOW = "Heaven Bow"
    SHIDGEDOU = "Shidgedou"
    WAR_BOW = "War Bow"
    ARBALEST = "Arbalest"
    FAILNAUGHT = "Failnaught"
    ZAMIEL_BOW = "Zamiel Bow"
    ARC_DRAWER = "Arc Drawer"
    LIGHT_WHIP = "Light Whip"
    FANG_WHIP = "Fang Whip"
    BULLWHIP = "Bullwhip"
    VINE_WHIP = "Vine Whip"
    NAIL_WHIP = "Nail Whip"
    EDGE_WHIP = "Edge Whip"
    TOXIC_WHIP = "Toxic Whip"
    GUM_WHIP = "Gum Whip"
    WIND_WHIP = "Wind Whip"
    SHRED_WHIP = "Shred Whip"
    STING_WHIP = "Sting Whip"
    BLADE_WHIP = "Blade Whip"
    NINE_TAILS = "Nine Tails"
    KNOUT = "Knout"
    DEAD_WHIP = "Dead Whip"
    TORMENTOR = "Tormentor"
    DOMINATOR = "Dominator"
    VOLT_WHIP = "Volt Whip"
    THORN_WHIP = "Thorn Whip"
    TWEED = "Tweed"
    JERKIN = "Jerkin"
    LEAF_COAT = "Leaf Coat"
    HIDE_VEST = "Hide Vest"
    HIDE_ARMOR = "Hide Armor"
    PLATE = "Plate"
    DOUBLET = "Doublet"
    BUFFCOAT = "Buffcoat"
    BRIAULT = "Briault"
    CHAIN_MAIL = "Chain Mail"
    PETAL_COAT = "Petal Coat"
    LEAF_TUNIC = "Leaf Tunic"
    IRON_PLATE = "Iron Plate"
    RING_MAIL = "Ring Mail"
    OAK_JACKET = "Oak Jacket"
    WING_COAT = "Wing Coat"
    HAUBERK = "Hauberk"
    STUD_VEST = "Stud Vest"
    FANCY_COAT = "Fancy Coat"
    COTARDIE = "Cotardie"
    FULL_ARMOR = "Full Armor"
    PLATE_MAIL = "Plate Mail"
    N7_DOUBLET = "7 Doublet"
    SURCOAT = "Surcoat"
    TIGER_COAT = "Tiger Coat"
    FAIRY_ROBE = "Fairy Robe"
    DARK_TUNIC = "Dark Tunic"
    BRIGANDINE = "Brigandine"
    EBON_PLATE = "Ebon Plate"
    LYCORIS = "Lycoris"
    WYVERNMAIL = "Wyvernmail"
    JAZERAINT = "Jazeraint"
    DEMON_COAT = "Demon Coat"
    RUNE_TWEED = "Rune Tweed"
    RUNE_TUNIC = "Rune Tunic"
    BLOOD_MAIL = "Blood Mail"
    COMPOSITE = "Composite"
    AZURE_COAT = "Azure Coat"
    BLOOD_COAT = "Blood Coat"
    DINO_PLATE = "Dino Plate"
    DEMON_MAIL = "Demon Mail"
    SYLPHEED = "Sylpheed"
    HOLY_ARMOR = "Holy Armor"
    GHOST_VEST = "Ghost Vest"
    MOBIUS_ALB = "Mobius Alb"
    ANGEL_ROBE = "Angel Robe"
    FAIRY_MAIL = "Fairy Mail"
    RUBY_MAIL = "Ruby Mail"
    HEX_MANTLE = "Hex Mantle"
    MOSS_COAT = "Moss Coat"
    FLAME_COAT = "Flame Coat"
    FROST_COAT = "Frost Coat"
    VOLT_COAT = "Volt Coat"
    HAIRPIN = "Hairpin"
    HIDE_HAT = "Hide Hat"
    PLUMED_HAT = "Plumed Hat"
    CHAIN_HELM = "Chain Helm"
    GUM_HELM = "Gum Helm"
    SCALE_HELM = "Scale Helm"
    SCALE_CAP = "Scale Cap"
    SANDY_PIN = "Sandy Pin"
    TIGER_CAP = "Tiger Cap"
    CIRCLET = "Circlet"
    BLOOD_HELM = "Blood Helm"
    ANGEL_HELM = "Angel Helm"
    KNIT_GLOVE = "Knit Glove"
    HIDE_GLOVE = "Hide Glove"
    DOWN_GLOVE = "Down Glove"
    IRON_GLOVE = "Iron Glove"
    BEAR_GLOVE = "Bear Glove"
    GUM_GLOVE = "Gum Glove"
    FANG_GLOVE = "Fang Glove"
    SAND_GLOVE = "Sand Glove"
    TIGER_HAND = "Tiger Hand"
    RUNE_GLOVE = "Rune Glove"
    BLOOD_GAGE = "Blood Gage"
    BRAVE_GAGE = "Brave Gage"
    EBON_GLOVE = "Ebon Glove"
    ATHANOR = "Athanor"
    RUBY_GAGE = "Ruby Gage"
    TOXIC_GAGE = "Toxic Gage"
    TARGE = "Targe"
    HIDE_ASPIS = "Hide Aspis"
    ASPIS = "Aspis"
    OVAL_ASPIS = "Oval Aspis"
    HEAT_ASPIS = "Heat Aspis"
    GUM_ASPIS = "Gum Aspis"
    BODY_ASPIS = "Body Aspis"
    EBON_ASPIS = "Ebon Aspis"
    MOON_ASPIS = "Moon Aspis"
    KING_ASPIS = "King Aspis"
    HALO_ASPIS = "Halo Aspis"
    HOLY_ASPIS = "Holy Aspis"
    PAIN_ASPIS = "Pain Aspis"
    LEAF_BOOT = "Leaf Boot"
    HIDE_BOOT = "Hide Boot"
    PLUME_BOOT = "Plume Boot"
    CHAIN_BOOT = "Chain Boot"
    MOCCASINS = "Moccasins"
    SCALE_BOOT = "Scale Boot"
    FAIRY_BOOT = "Fairy Boot"
    TIGER_BOOT = "Tiger Boot"
    FLAME_BOOT = "Flame Boot"
    FUR_BOOT = "Fur Boot"
    DYED_BOOT = "Dyed Boot"
    SPEED_BOOT = "Speed Boot"
    HIDE_BELT = "Hide Belt"
    HIDE_RING = "Hide Ring"
    RED_CHARM = "Red Charm"
    PETAL_RING = "Petal Ring"
    CUT_CHARM = "Cut Charm"
    GEM_RING = "Gem Ring"
    LEAF_CAPE = "Leaf Cape"
    FIRE_RING = "Fire Ring"
    STAR_CHARM = "Star Charm"
    TUSK_CHARM = "Tusk Charm"
    OLD_CHOKER = "Old Choker"
    HIDE_CAPE = "Hide Cape"
    AMBER_RING = "Amber Ring"
    SEA_CHARM = "Sea Charm"
    BLUE_RING = "Blue Ring"
    RED_CAPE = "Red Cape"
    EVIL_CHARM = "Evil Charm"
    ROSE_RING = "Rose Ring"
    ROYAL_RING = "Royal Ring"
    GOLD_CAPE = "Gold Cape"
    ANGEL_RING = "Angel Ring"
    WARD_GEM = "Ward Gem"
    JEWEL_EYE = "Jewel Eye"
    RUBY = "Ruby"
    SAPPHIRE = "Sapphire"
    TOPAZ = "Topaz"
    TOURMALINE = "Tourmaline"
    ADAMAS = "Adamas"
    HEX_DOLL = "Hex Doll"
    OCARINA = "Ocarina"
    LUTE = "Lute"
    FLUTE = "Flute"
    KITHARA = "Kithara"
    AULOS = "Aulos"
    ANGEL_HARP = "Angel Harp"
    SYRINX = "Syrinx"
    TOWN_MEDAL = "Town Medal"
    TOWN_CROWN = "Town Crown"
    MOSS_RING = "Moss Ring"
    MOSS_BAND = "Moss Band"

CONSUMABLE_DATA: list[EO1ItemData] = [
    EO1ItemData(EO1ItemType.Consumable, 0x10B7, EO1ItemNames.MEDICA, 1001, ItemClassification.filler, weight=50),
    EO1ItemData(EO1ItemType.Consumable, 0x10B8, EO1ItemNames.MEDICA_II, 1002, ItemClassification.filler, weight=75),
    EO1ItemData(EO1ItemType.Consumable, 0x10B9, EO1ItemNames.MEDICA_III, 1003, ItemClassification.filler | ItemClassification.useful, weight=75),
    EO1ItemData(EO1ItemType.Consumable, 0x10BA, EO1ItemNames.MEDICA_IV, 1004, ItemClassification.filler | ItemClassification.useful, weight=75),
    EO1ItemData(EO1ItemType.Consumable, 0x10BB, EO1ItemNames.MEDICA_V, 1005, ItemClassification.filler | ItemClassification.useful, weight=50),
    EO1ItemData(EO1ItemType.Consumable, 0x10BC, EO1ItemNames.AMRITA, 1006, ItemClassification.filler | ItemClassification.useful, weight=50),
    EO1ItemData(EO1ItemType.Consumable, 0x10BD, EO1ItemNames.AMRITA_II, 1007, ItemClassification.filler | ItemClassification.useful, weight=35),
    EO1ItemData(EO1ItemType.Consumable, 0x10BE, EO1ItemNames.HAMAO, 1008, ItemClassification.filler | ItemClassification.useful, weight=10),
    EO1ItemData(EO1ItemType.Consumable, 0x10BF, EO1ItemNames.HAMAOPRIME, 1009, ItemClassification.filler | ItemClassification.useful, weight=1),
    EO1ItemData(EO1ItemType.Consumable, 0x10C0, EO1ItemNames.SOMA, 1010, ItemClassification.filler | ItemClassification.useful, weight=10),
    EO1ItemData(EO1ItemType.Consumable, 0x10C1, EO1ItemNames.SOMAPRIME, 1011, ItemClassification.filler | ItemClassification.useful, weight=1),
    EO1ItemData(EO1ItemType.Consumable, 0x10C2, EO1ItemNames.NECTAR, 1012, ItemClassification.filler | ItemClassification.useful, weight=25),
    EO1ItemData(EO1ItemType.Consumable, 0x10C3, EO1ItemNames.NECTAR_II, 1013, ItemClassification.filler | ItemClassification.useful, weight=25),
    EO1ItemData(EO1ItemType.Consumable, 0x10C4, EO1ItemNames.NECTAR_III, 1014, ItemClassification.filler | ItemClassification.useful, weight=5),
    EO1ItemData(EO1ItemType.Consumable, 0x10C7, EO1ItemNames.THERIACA_A, 1015, ItemClassification.filler | ItemClassification.useful, weight=40),
    EO1ItemData(EO1ItemType.Consumable, 0x10C8, EO1ItemNames.THERIACA_B, 1016, ItemClassification.filler | ItemClassification.useful, weight=40),
    EO1ItemData(EO1ItemType.Consumable, 0x10CD, EO1ItemNames.AXCELA, 1017, ItemClassification.filler, weight=20),
    EO1ItemData(EO1ItemType.Consumable, 0x10CE, EO1ItemNames.AXCELA_II, 1018, ItemClassification.filler | ItemClassification.useful, weight=15),
    EO1ItemData(EO1ItemType.Consumable, 0x10CF, EO1ItemNames.AXCELA_III, 1019, ItemClassification.filler | ItemClassification.useful, weight=5),
    EO1ItemData(EO1ItemType.Consumable, 0x10D1, EO1ItemNames.BRAVANT, 1020, ItemClassification.filler | ItemClassification.useful, weight=30),
    EO1ItemData(EO1ItemType.Consumable, 0x10D2, EO1ItemNames.BRAVANT_II, 1021, ItemClassification.filler | ItemClassification.useful, weight=10),
    EO1ItemData(EO1ItemType.Consumable, 0x10D3, EO1ItemNames.STONARD, 1022, ItemClassification.filler, weight=30),
    EO1ItemData(EO1ItemType.Consumable, 0x10D4, EO1ItemNames.STONARD_II, 1023, ItemClassification.filler | ItemClassification.useful, weight=10),
    EO1ItemData(EO1ItemType.Consumable, 0x10D7, EO1ItemNames.FIRE_MIST, 1024, ItemClassification.filler | ItemClassification.useful, weight=10),
    EO1ItemData(EO1ItemType.Consumable, 0x10D8, EO1ItemNames.ICE_MIST, 1025, ItemClassification.filler | ItemClassification.useful, weight=10),
    EO1ItemData(EO1ItemType.Consumable, 0x10D9, EO1ItemNames.VOLT_MIST, 1026, ItemClassification.filler | ItemClassification.useful, weight=10),
    EO1ItemData(EO1ItemType.Consumable, 0x10DA, EO1ItemNames.ALL_MIST, 1027, ItemClassification.filler | ItemClassification.useful, weight=5),
    EO1ItemData(EO1ItemType.Consumable, 0x10DB, EO1ItemNames.BLAZE_OIL, 1028, ItemClassification.filler | ItemClassification.useful, weight=10),
    EO1ItemData(EO1ItemType.Consumable, 0x10DC, EO1ItemNames.FREEZE_OIL, 1029, ItemClassification.filler | ItemClassification.useful, weight=10),
    EO1ItemData(EO1ItemType.Consumable, 0x10DD, EO1ItemNames.SHOCK_OIL, 1030, ItemClassification.filler | ItemClassification.useful, weight=10),
    EO1ItemData(EO1ItemType.Consumable, 0x10DF, EO1ItemNames.WARD_CHIME, 1031, ItemClassification.filler, weight=5),
    EO1ItemData(EO1ItemType.Consumable, 0x10E0, EO1ItemNames.GOLD_CHIME, 1032, ItemClassification.filler, weight=5),
    EO1ItemData(EO1ItemType.Consumable, 0x10EC, EO1ItemNames.MAGNET, 1034, ItemClassification.filler, weight=5),
    EO1ItemData(EO1ItemType.Consumable, 0x1116, EO1ItemNames.WARP_WIRE, 1035, ItemClassification.useful, weight=5)
]

KEY_ITEM_DATA: list[EO1KeyItem] = [
    EO1KeyItem(0x1102, EO1ItemNames.CLEAR_KEY, 1056, 0x41),
    EO1KeyItem(0x1103, EO1ItemNames.VIOLET_KEY, 1057, 0x42),

    # EO1ItemData(EO1ItemType.Key, 0x1104, EO1ItemNames.DRAGON_EGG, 1058),
    # EO1ItemData(EO1ItemType.Key, 0x1105, EO1ItemNames.CARD_KEY, 1059),

    # EO1ItemData(EO1ItemType.Key, 0x1112, EO1ItemNames.OLD_SCROLL, 1072),
    # EO1ItemData(EO1ItemType.Key, 0x1113, EO1ItemNames.HEX_BELL, 1073),
    # EO1ItemData(EO1ItemType.Key, 0x1114, EO1ItemNames.MAP, 1074),
    # EO1ItemData(EO1ItemType.Key, 0x1115, EO1ItemNames.RADHA_NOTE, 1075),

    #EO1ItemData(EO1ItemType.Key, 0x103C, EO1ItemNames.JADE_ORE, 1000),
    #EO1ItemData(EO1ItemType.Key, 0x10ED, EO1ItemNames.MAP_EVENT, 1035),
    #EO1ItemData(EO1ItemType.Key, 0x10EE, EO1ItemNames.HOLY_WATER, 1036),
    #EO1ItemData(EO1ItemType.Key, 0x10EF, EO1ItemNames.WATER, 1037),
    #EO1ItemData(EO1ItemType.Key, 0x10F0, EO1ItemNames.BOTTLE, 1038),
    #EO1ItemData(EO1ItemType.Key, 0x10F1, EO1ItemNames.JUNK_BOX, 1039),
    #EO1ItemData(EO1ItemType.Key, 0x10F2, EO1ItemNames.JUNK_BOX, 1040),
    #EO1ItemData(EO1ItemType.Key, 0x10F3, EO1ItemNames.LOCKET, 1041),
    #EO1ItemData(EO1ItemType.Key, 0x10F4, EO1ItemNames.PLANT_SEED, 1042),
    #EO1ItemData(EO1ItemType.Key, 0x10F5, EO1ItemNames.GOLD_STONE, 1043),
    #EO1ItemData(EO1ItemType.Key, 0x10F6, EO1ItemNames.GOLD_STONE, 1044),
    #EO1ItemData(EO1ItemType.Key, 0x10F7, EO1ItemNames.MOON_STONE, 1045),
    #EO1ItemData(EO1ItemType.Key, 0x10F8, EO1ItemNames.GOUDA, 1046),
    #EO1ItemData(EO1ItemType.Key, 0x10F9, EO1ItemNames.ODD_POWDER, 1047),
    #EO1ItemData(EO1ItemType.Key, 0x10FA, EO1ItemNames.LUCKY_COIN, 1048),
    #EO1ItemData(EO1ItemType.Key, 0x10FB, EO1ItemNames.RUST_SWORD, 1049),
    #EO1ItemData(EO1ItemType.Key, 0x10FC, EO1ItemNames.BROKEN_AXE, 1050),
    #EO1ItemData(EO1ItemType.Key, 0x10FD, EO1ItemNames.OLD_WAND, 1051),
    #EO1ItemData(EO1ItemType.Key, 0x10FE, EO1ItemNames.PANACEA, 1052),
    #EO1ItemData(EO1ItemType.Key, 0x10FF, EO1ItemNames.RARE_BLOOM, 1053),
    #EO1ItemData(EO1ItemType.Key, 0x1100, EO1ItemNames.GOLD_SEED, 1054),
    #EO1ItemData(EO1ItemType.Key, 0x1101, EO1ItemNames.VOX_STONE, 1055),
    #EO1ItemData(EO1ItemType.Key, 0x1106, EO1ItemNames.HOLY_GRAIL, 1060),
    #EO1ItemData(EO1ItemType.Key, 0x1107, EO1ItemNames.COPPER_TOP, 1061),
    #EO1ItemData(EO1ItemType.Key, 0x1108, EO1ItemNames.SHINY_DISC, 1062),
    #EO1ItemData(EO1ItemType.Key, 0x1109, EO1ItemNames.SOFT_GLASS, 1063),
    #EO1ItemData(EO1ItemType.Key, 0x110A, EO1ItemNames.TOKEN, 1064),
    #EO1ItemData(EO1ItemType.Key, 0x110B, EO1ItemNames.CLAM_TOOL, 1065),
    #EO1ItemData(EO1ItemType.Key, 0x110C, EO1ItemNames.MAGIC_DOWN, 1066),
    #EO1ItemData(EO1ItemType.Key, 0x110D, EO1ItemNames.MAGIC_DOWN, 1067),
    #EO1ItemData(EO1ItemType.Key, 0x110E, EO1ItemNames.MAGIC_DOWN, 1068),
    #EO1ItemData(EO1ItemType.Key, 0x110F, EO1ItemNames.DIAMOND, 1069),
    #EO1ItemData(EO1ItemType.Key, 0x1110, EO1ItemNames.BLACK_GEM, 1070),
    #EO1ItemData(EO1ItemType.Key, 0x1111, EO1ItemNames.SHINY_GEM, 1071),
    #EO1ItemData(EO1ItemType.Key, 0x1117, EO1ItemNames.TOUGH_FANG, 1077),
    #EO1ItemData(EO1ItemType.Key, 0x1119, EO1ItemNames.TOUGH_WING, 1078),
    #EO1ItemData(EO1ItemType.Key, 0x113D, EO1ItemNames.FROZEN_ARM, 1079),
    #EO1ItemData(EO1ItemType.Key, 0x113E, EO1ItemNames.ANKH_A, 1080),
    #EO1ItemData(EO1ItemType.Key, 0x113F, EO1ItemNames.ANKH_B, 1081),
    #EO1ItemData(EO1ItemType.Key, 0x1140, EO1ItemNames.ANKH_C, 1082),
    #EO1ItemData(EO1ItemType.Key, 0x1141, EO1ItemNames.ANKH_D, 1083),
    #EO1ItemData(EO1ItemType.Key, 0x1142, EO1ItemNames.ANKH_E, 1084),
    #EO1ItemData(EO1ItemType.Key, 0x1143, EO1ItemNames.ANKH_MOTOR, 1085),
    #EO1ItemData(EO1ItemType.Key, 0x1144, EO1ItemNames.BANDANNA, 1086),
    #EO1ItemData(EO1ItemType.Key, 0x1145, EO1ItemNames.PEARL, 1087),
    #EO1ItemData(EO1ItemType.Key, 0x1146, EO1ItemNames.RARE_MEAT, 1088),
]

QUEST_ITEM_DATA: list[EO1ItemData] = [
    # Placeholder for future feature.
]


SWORD_DATA: list[EO1EquipmentData] = [
    EO1EquipmentData(EO1ItemType.Equipment, 0x001, EO1EquipmentNames.KNIFE, 2000, EO1EquipmentType.Sword), # DmgType: Slash, Secondary DmgType: None, ATK: 6, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x002, EO1EquipmentNames.SCRAMASAX, 2001, EO1EquipmentType.Sword), # DmgType: Slash, Secondary DmgType: None, ATK: 8, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x003, EO1EquipmentNames.DAGGER, 2002, EO1EquipmentType.Sword), # DmgType: Slash, Secondary DmgType: None, ATK: 9, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x004, EO1EquipmentNames.SHORTSWORD, 2003, EO1EquipmentType.Sword), # DmgType: Slash, Secondary DmgType: None, ATK: 15, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x005, EO1EquipmentNames.BOAR_SPEAR, 2004, EO1EquipmentType.Sword), # DmgType: Slash, Secondary DmgType: None, ATK: 29, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x006, EO1EquipmentNames.BROADSWORD, 2005, EO1EquipmentType.Sword), # DmgType: Slash, Secondary DmgType: None, ATK: 34, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x007, EO1EquipmentNames.RAPIER, 2006, EO1EquipmentType.Sword), # DmgType: Slash, Secondary DmgType: None, ATK: 45, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x008, EO1EquipmentNames.VIKING, 2007, EO1EquipmentType.Sword), # DmgType: Slash, Secondary DmgType: None, ATK: 57, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x009, EO1EquipmentNames.SHAMSHIR, 2008, EO1EquipmentType.Sword), # DmgType: Slash, Secondary DmgType: None, ATK: 63, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x00A, EO1EquipmentNames.CLAYMORE, 2009, EO1EquipmentType.Sword), # DmgType: Slash, Secondary DmgType: None, ATK: 78, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x00B, EO1EquipmentNames.EXECUTOR, 2010, EO1EquipmentType.Sword), # DmgType: Slash, Secondary DmgType: None, ATK: 97, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x00C, EO1EquipmentNames.KATZBALGER, 2011, EO1EquipmentType.Sword), # DmgType: Slash, Secondary DmgType: None, ATK: 106, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x00D, EO1EquipmentNames.STEELSWORD, 2012, EO1EquipmentType.Sword), # DmgType: Slash, Secondary DmgType: None, ATK: 125, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x00E, EO1EquipmentNames.EPEE, 2013, EO1EquipmentType.Sword), # DmgType: Slash, Secondary DmgType: None, ATK: 139, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x00F, EO1EquipmentNames.LAST_ESTOC, 2014, EO1EquipmentType.Sword), # DmgType: Slash, Secondary DmgType: None, ATK: 151, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x010, EO1EquipmentNames.PATTISA, 2015, EO1EquipmentType.Sword), # DmgType: Slash, Secondary DmgType: None, ATK: 167, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x011, EO1EquipmentNames.FLAMBERGE, 2016, EO1EquipmentType.Sword), # DmgType: Slash, Secondary DmgType: None, ATK: 182, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x015, EO1EquipmentNames.DUERGAR, 2017, EO1EquipmentType.Sword), # DmgType: Slash, Secondary DmgType: None, ATK: 200, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x017, EO1EquipmentNames.SHINRYUU, 2018, EO1EquipmentType.Sword), # DmgType: Slash, Secondary DmgType: None, ATK: 250, DEF: 0
]

STAFF_DATA: list[EO1EquipmentData] = [
    EO1EquipmentData(EO1ItemType.Equipment, 0x028, EO1EquipmentNames.WAND, 2019, EO1EquipmentType.Staff), # DmgType: Bash, Secondary DmgType: None, ATK: 3, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x036, EO1EquipmentNames.STAFF, 2020, EO1EquipmentType.Staff), # DmgType: Bash, Secondary DmgType: None, ATK: 3, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x037, EO1EquipmentNames.BONE_STAFF, 2021, EO1EquipmentType.Staff), # DmgType: Bash, Secondary DmgType: None, ATK: 5, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x038, EO1EquipmentNames.BONE_MACE, 2022, EO1EquipmentType.Staff), # DmgType: Bash, Secondary DmgType: None, ATK: 15, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x039, EO1EquipmentNames.DOWN_STAFF, 2023, EO1EquipmentType.Staff), # DmgType: Bash, Secondary DmgType: None, ATK: 22, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x03A, EO1EquipmentNames.BONE_FLAIL, 2024, EO1EquipmentType.Staff), # DmgType: Bash, Secondary DmgType: None, ATK: 47, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x03B, EO1EquipmentNames.GEM_STAFF, 2025, EO1EquipmentType.Staff), # DmgType: Bash, Secondary DmgType: None, ATK: 53, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x03C, EO1EquipmentNames.WAR_MACE, 2026, EO1EquipmentType.Staff), # DmgType: Bash, Secondary DmgType: None, ATK: 70, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x03D, EO1EquipmentNames.LUCK_STAFF, 2027, EO1EquipmentType.Staff), # DmgType: Bash, Secondary DmgType: None, ATK: 78, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x03E, EO1EquipmentNames.GODENDAG, 2028, EO1EquipmentType.Staff), # DmgType: Bash, Secondary DmgType: None, ATK: 99, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x03F, EO1EquipmentNames.MYSTIC_ROD, 2029, EO1EquipmentType.Staff), # DmgType: Bash, Secondary DmgType: None, ATK: 109, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x040, EO1EquipmentNames.WARHAMMER, 2030, EO1EquipmentType.Staff), # DmgType: Bash, Secondary DmgType: None, ATK: 131, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x041, EO1EquipmentNames.ARCANA_ROD, 2031, EO1EquipmentType.Staff), # DmgType: Bash, Secondary DmgType: None, ATK: 100, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x042, EO1EquipmentNames.SAGE_WAND, 2032, EO1EquipmentType.Staff), # DmgType: Bash, Secondary DmgType: None, ATK: 150, DEF: 0
]

AXE_DATA: list[EO1EquipmentData] = [
    EO1EquipmentData(EO1ItemType.Equipment, 0x01E, EO1EquipmentNames.BONE_AXE, 2033, EO1EquipmentType.Axe), # DmgType: Slash, Secondary DmgType: None, ATK: 11, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x01F, EO1EquipmentNames.HAND_AXE, 2034, EO1EquipmentType.Axe), # DmgType: Slash, Secondary DmgType: None, ATK: 18, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x020, EO1EquipmentNames.CELTIS, 2035, EO1EquipmentType.Axe), # DmgType: Slash, Secondary DmgType: None, ATK: 32, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x021, EO1EquipmentNames.BROADAXE, 2036, EO1EquipmentType.Axe), # DmgType: Slash, Secondary DmgType: None, ATK: 44, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x022, EO1EquipmentNames.BATTLE_AXE, 2037, EO1EquipmentType.Axe), # DmgType: Slash, Secondary DmgType: None, ATK: 58, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x023, EO1EquipmentNames.BILIOMG, 2038, EO1EquipmentType.Axe), # DmgType: Slash, Secondary DmgType: None, ATK: 77, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x024, EO1EquipmentNames.TABAR, 2039, EO1EquipmentType.Axe), # DmgType: Slash, Secondary DmgType: None, ATK: 86, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x025, EO1EquipmentNames.GREAT_AXE, 2040, EO1EquipmentType.Axe), # DmgType: Slash, Secondary DmgType: None, ATK: 97, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x026, EO1EquipmentNames.BARDICHE, 2041, EO1EquipmentType.Axe), # DmgType: Slash, Secondary DmgType: None, ATK: 104, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x027, EO1EquipmentNames.HALBERD, 2042, EO1EquipmentType.Axe), # DmgType: Slash, Secondary DmgType: None, ATK: 116, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x029, EO1EquipmentNames.BREAKER, 2043, EO1EquipmentType.Axe), # DmgType: Slash, Secondary DmgType: None, ATK: 151, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x02A, EO1EquipmentNames.LABYRIS, 2044, EO1EquipmentType.Axe), # DmgType: Slash, Secondary DmgType: None, ATK: 162, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x02B, EO1EquipmentNames.FRANCISCA, 2045, EO1EquipmentType.Axe), # DmgType: Slash, Secondary DmgType: None, ATK: 179, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x02C, EO1EquipmentNames.BHUJ, 2046, EO1EquipmentType.Axe), # DmgType: Slash, Secondary DmgType: None, ATK: 198, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x02D, EO1EquipmentNames.FASCES_AXE, 2047, EO1EquipmentType.Axe), # DmgType: Slash, Secondary DmgType: None, ATK: 207, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x030, EO1EquipmentNames.FLAME_AXE, 2048, EO1EquipmentType.Axe), # DmgType: Slash, Secondary DmgType: Fire, ATK: 200, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x031, EO1EquipmentNames.METEOR_AXE, 2049, EO1EquipmentType.Axe), # DmgType: Slash, Secondary DmgType: None, ATK: 240, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x032, EO1EquipmentNames.HATCHET, 2050, EO1EquipmentType.Axe), # DmgType: Slash, Secondary DmgType: None, ATK: 9, DEF: 0
]

KATANA_DATA: list[EO1EquipmentData] = [
    EO1EquipmentData(EO1ItemType.Equipment, 0x049, EO1EquipmentNames.WAKIZASHI, 2051, EO1EquipmentType.Katana), # DmgType: Slash, Secondary DmgType: None, ATK: 20, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x04A, EO1EquipmentNames.UCHIGATANA, 2052, EO1EquipmentType.Katana), # DmgType: Slash, Secondary DmgType: None, ATK: 55, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x04B, EO1EquipmentNames.OHDACHI, 2053, EO1EquipmentType.Katana), # DmgType: Slash, Secondary DmgType: None, ATK: 90, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x04C, EO1EquipmentNames.KOGARASU, 2054, EO1EquipmentType.Katana), # DmgType: Slash, Secondary DmgType: None, ATK: 119, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x04D, EO1EquipmentNames.SHIDA, 2055, EO1EquipmentType.Katana), # DmgType: Slash, Secondary DmgType: None, ATK: 149, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x04E, EO1EquipmentNames.ZANMATOU, 2056, EO1EquipmentType.Katana), # DmgType: Slash, Secondary DmgType: None, ATK: 170, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x04F, EO1EquipmentNames.KUZUNOSADA, 2057, EO1EquipmentType.Katana), # DmgType: Slash, Secondary DmgType: None, ATK: 209, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x050, EO1EquipmentNames.HACHI, 2058, EO1EquipmentType.Katana), # DmgType: Slash, Secondary DmgType: None, ATK: 215, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x051, EO1EquipmentNames.HISAMEMARU, 2059, EO1EquipmentType.Katana), # DmgType: Slash, Secondary DmgType: Ice, ATK: 229, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x052, EO1EquipmentNames.MASAMUNE, 2060, EO1EquipmentType.Katana), # DmgType: Slash, Secondary DmgType: None, ATK: 240, DEF: 0
]

BOW_DATA: list[EO1EquipmentData] = [
    EO1EquipmentData(EO1ItemType.Equipment, 0x058, EO1EquipmentNames.WOOD_BOW, 2061, EO1EquipmentType.Bow), # DmgType: Pierce, Secondary DmgType: None, ATK: 7, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x059, EO1EquipmentNames.ENAMEL_BOW, 2062, EO1EquipmentType.Bow), # DmgType: Pierce, Secondary DmgType: None, ATK: 9, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x05A, EO1EquipmentNames.SHORT_BOW, 2063, EO1EquipmentType.Bow), # DmgType: Pierce, Secondary DmgType: None, ATK: 15, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x05B, EO1EquipmentNames.BEAST_BOW, 2064, EO1EquipmentType.Bow), # DmgType: Pierce, Secondary DmgType: None, ATK: 24, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x05C, EO1EquipmentNames.HARD_SLING, 2065, EO1EquipmentType.Bow), # DmgType: Pierce, Secondary DmgType: None, ATK: 30, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x05D, EO1EquipmentNames.LONG_BOW, 2066, EO1EquipmentType.Bow), # DmgType: Pierce, Secondary DmgType: None, ATK: 39, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x05E, EO1EquipmentNames.HINDI, 2067, EO1EquipmentType.Bow), # DmgType: Pierce, Secondary DmgType: None, ATK: 49, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x05F, EO1EquipmentNames.SELF_BOW, 2068, EO1EquipmentType.Bow), # DmgType: Pierce, Secondary DmgType: None, ATK: 59, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x060, EO1EquipmentNames.HUNTER_BOW, 2069, EO1EquipmentType.Bow), # DmgType: Pierce, Secondary DmgType: None, ATK: 75, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x061, EO1EquipmentNames.FIN_BOW, 2070, EO1EquipmentType.Bow), # DmgType: Pierce, Secondary DmgType: None, ATK: 88, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x062, EO1EquipmentNames.VINE_BOW, 2071, EO1EquipmentType.Bow), # DmgType: Pierce, Secondary DmgType: None, ATK: 97, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x063, EO1EquipmentNames.HEAVEN_BOW, 2072, EO1EquipmentType.Bow), # DmgType: Pierce, Secondary DmgType: None, ATK: 111, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x064, EO1EquipmentNames.SHIDGEDOU, 2073, EO1EquipmentType.Bow), # DmgType: Pierce, Secondary DmgType: None, ATK: 123, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x065, EO1EquipmentNames.WAR_BOW, 2074, EO1EquipmentType.Bow), # DmgType: Pierce, Secondary DmgType: None, ATK: 140, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x066, EO1EquipmentNames.ARBALEST, 2075, EO1EquipmentType.Bow), # DmgType: Pierce, Secondary DmgType: None, ATK: 161, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x067, EO1EquipmentNames.FAILNAUGHT, 2076, EO1EquipmentType.Bow), # DmgType: Pierce, Secondary DmgType: None, ATK: 181, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x069, EO1EquipmentNames.ZAMIEL_BOW, 2077, EO1EquipmentType.Bow), # DmgType: Pierce, Secondary DmgType: None, ATK: 202, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x06A, EO1EquipmentNames.ARC_DRAWER, 2078, EO1EquipmentType.Bow), # DmgType: Pierce, Secondary DmgType: None, ATK: 220, DEF: 0
]

WHIP_DATA: list[EO1EquipmentData] = [
    EO1EquipmentData(EO1ItemType.Equipment, 0x070, EO1EquipmentNames.LIGHT_WHIP, 2079, EO1EquipmentType.Whip), # DmgType: Slash, Secondary DmgType: None, ATK: 7, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x071, EO1EquipmentNames.FANG_WHIP, 2080, EO1EquipmentType.Whip), # DmgType: Slash, Secondary DmgType: None, ATK: 10, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x072, EO1EquipmentNames.BULLWHIP, 2081, EO1EquipmentType.Whip), # DmgType: Slash, Secondary DmgType: None, ATK: 16, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x073, EO1EquipmentNames.VINE_WHIP, 2082, EO1EquipmentType.Whip), # DmgType: Slash, Secondary DmgType: None, ATK: 28, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x074, EO1EquipmentNames.NAIL_WHIP, 2083, EO1EquipmentType.Whip), # DmgType: Slash, Secondary DmgType: None, ATK: 38, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x075, EO1EquipmentNames.EDGE_WHIP, 2084, EO1EquipmentType.Whip), # DmgType: Slash, Secondary DmgType: None, ATK: 49, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x076, EO1EquipmentNames.TOXIC_WHIP, 2085, EO1EquipmentType.Whip), # DmgType: Slash, Secondary DmgType: None, ATK: 57, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x077, EO1EquipmentNames.GUM_WHIP, 2086, EO1EquipmentType.Whip), # DmgType: Slash, Secondary DmgType: None, ATK: 70, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x078, EO1EquipmentNames.WIND_WHIP, 2087, EO1EquipmentType.Whip), # DmgType: Slash, Secondary DmgType: None, ATK: 79, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x079, EO1EquipmentNames.SHRED_WHIP, 2088, EO1EquipmentType.Whip), # DmgType: Slash, Secondary DmgType: None, ATK: 94, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x07A, EO1EquipmentNames.STING_WHIP, 2089, EO1EquipmentType.Whip), # DmgType: Slash, Secondary DmgType: None, ATK: 103, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x07B, EO1EquipmentNames.BLADE_WHIP, 2090, EO1EquipmentType.Whip), # DmgType: Slash, Secondary DmgType: None, ATK: 115, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x07C, EO1EquipmentNames.NINE_TAILS, 2091, EO1EquipmentType.Whip), # DmgType: Slash, Secondary DmgType: None, ATK: 125, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x07D, EO1EquipmentNames.KNOUT, 2092, EO1EquipmentType.Whip), # DmgType: Slash, Secondary DmgType: None, ATK: 136, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x07E, EO1EquipmentNames.DEAD_WHIP, 2093, EO1EquipmentType.Whip), # DmgType: Slash, Secondary DmgType: None, ATK: 157, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x07F, EO1EquipmentNames.TORMENTOR, 2094, EO1EquipmentType.Whip), # DmgType: Slash, Secondary DmgType: None, ATK: 175, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x081, EO1EquipmentNames.DOMINATOR, 2095, EO1EquipmentType.Whip), # DmgType: Slash, Secondary DmgType: None, ATK: 180, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x083, EO1EquipmentNames.VOLT_WHIP, 2096, EO1EquipmentType.Whip), # DmgType: Slash, Secondary DmgType: Volt, ATK: 200, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0x084, EO1EquipmentNames.THORN_WHIP, 2097, EO1EquipmentType.Whip), # DmgType: Slash, Secondary DmgType: None, ATK: 195, DEF: 0
]

ARMOR_DATA: list[EO1EquipmentData] = [
    EO1EquipmentData(EO1ItemType.Equipment, 0x3E9, EO1EquipmentNames.TWEED, 2098, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0x3EA, EO1EquipmentNames.JERKIN, 2099, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 3
    EO1EquipmentData(EO1ItemType.Equipment, 0x3EB, EO1EquipmentNames.LEAF_COAT, 2100, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0x3EC, EO1EquipmentNames.HIDE_VEST, 2101, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 2
    EO1EquipmentData(EO1ItemType.Equipment, 0x3ED, EO1EquipmentNames.HIDE_ARMOR, 2102, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 4
    EO1EquipmentData(EO1ItemType.Equipment, 0x3EE, EO1EquipmentNames.PLATE, 2103, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 5
    EO1EquipmentData(EO1ItemType.Equipment, 0x3EF, EO1EquipmentNames.DOUBLET, 2104, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 3
    EO1EquipmentData(EO1ItemType.Equipment, 0x3F0, EO1EquipmentNames.BUFFCOAT, 2105, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 2
    EO1EquipmentData(EO1ItemType.Equipment, 0x3F1, EO1EquipmentNames.BRIAULT, 2106, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 5
    EO1EquipmentData(EO1ItemType.Equipment, 0x3F2, EO1EquipmentNames.CHAIN_MAIL, 2107, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 7
    EO1EquipmentData(EO1ItemType.Equipment, 0x3F3, EO1EquipmentNames.PETAL_COAT, 2108, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 4
    EO1EquipmentData(EO1ItemType.Equipment, 0x3F4, EO1EquipmentNames.LEAF_TUNIC, 2109, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 6
    EO1EquipmentData(EO1ItemType.Equipment, 0x3F5, EO1EquipmentNames.IRON_PLATE, 2110, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 12
    EO1EquipmentData(EO1ItemType.Equipment, 0x3F6, EO1EquipmentNames.RING_MAIL, 2111, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 16
    EO1EquipmentData(EO1ItemType.Equipment, 0x3F7, EO1EquipmentNames.OAK_JACKET, 2112, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 8
    EO1EquipmentData(EO1ItemType.Equipment, 0x3F8, EO1EquipmentNames.WING_COAT, 2113, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 6
    EO1EquipmentData(EO1ItemType.Equipment, 0x3F9, EO1EquipmentNames.HAUBERK, 2114, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 10
    EO1EquipmentData(EO1ItemType.Equipment, 0x3FB, EO1EquipmentNames.STUD_VEST, 2115, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 17
    EO1EquipmentData(EO1ItemType.Equipment, 0x3FC, EO1EquipmentNames.FANCY_COAT, 2116, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 11
    EO1EquipmentData(EO1ItemType.Equipment, 0x3FD, EO1EquipmentNames.COTARDIE, 2117, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 16
    EO1EquipmentData(EO1ItemType.Equipment, 0x3FE, EO1EquipmentNames.FULL_ARMOR, 2118, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 22
    EO1EquipmentData(EO1ItemType.Equipment, 0x3FF, EO1EquipmentNames.PLATE_MAIL, 2119, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 26
    EO1EquipmentData(EO1ItemType.Equipment, 0x400, EO1EquipmentNames.N7_DOUBLET, 2120, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 18
    EO1EquipmentData(EO1ItemType.Equipment, 0x401, EO1EquipmentNames.SURCOAT, 2121, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 16
    EO1EquipmentData(EO1ItemType.Equipment, 0x403, EO1EquipmentNames.TIGER_COAT, 2122, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 27
    EO1EquipmentData(EO1ItemType.Equipment, 0x404, EO1EquipmentNames.FAIRY_ROBE, 2123, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 24
    EO1EquipmentData(EO1ItemType.Equipment, 0x405, EO1EquipmentNames.DARK_TUNIC, 2124, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 26
    EO1EquipmentData(EO1ItemType.Equipment, 0x406, EO1EquipmentNames.BRIGANDINE, 2125, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 32
    EO1EquipmentData(EO1ItemType.Equipment, 0x407, EO1EquipmentNames.EBON_PLATE, 2126, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 36
    EO1EquipmentData(EO1ItemType.Equipment, 0x408, EO1EquipmentNames.LYCORIS, 2127, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 28
    EO1EquipmentData(EO1ItemType.Equipment, 0x409, EO1EquipmentNames.WYVERNMAIL, 2128, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 26
    EO1EquipmentData(EO1ItemType.Equipment, 0x40A, EO1EquipmentNames.JAZERAINT, 2129, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 35
    EO1EquipmentData(EO1ItemType.Equipment, 0x40B, EO1EquipmentNames.DEMON_COAT, 2130, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 37
    EO1EquipmentData(EO1ItemType.Equipment, 0x40C, EO1EquipmentNames.RUNE_TWEED, 2131, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 24
    EO1EquipmentData(EO1ItemType.Equipment, 0x40D, EO1EquipmentNames.RUNE_TUNIC, 2132, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 36
    EO1EquipmentData(EO1ItemType.Equipment, 0x40E, EO1EquipmentNames.BLOOD_MAIL, 2133, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 42
    EO1EquipmentData(EO1ItemType.Equipment, 0x40F, EO1EquipmentNames.COMPOSITE, 2134, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 46
    EO1EquipmentData(EO1ItemType.Equipment, 0x410, EO1EquipmentNames.AZURE_COAT, 2135, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 38
    EO1EquipmentData(EO1ItemType.Equipment, 0x411, EO1EquipmentNames.BLOOD_COAT, 2136, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 36
    EO1EquipmentData(EO1ItemType.Equipment, 0x412, EO1EquipmentNames.DINO_PLATE, 2137, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 32
    EO1EquipmentData(EO1ItemType.Equipment, 0x413, EO1EquipmentNames.DEMON_MAIL, 2138, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 52
    EO1EquipmentData(EO1ItemType.Equipment, 0x414, EO1EquipmentNames.SYLPHEED, 2139, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 47
    EO1EquipmentData(EO1ItemType.Equipment, 0x415, EO1EquipmentNames.HOLY_ARMOR, 2140, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 56
    EO1EquipmentData(EO1ItemType.Equipment, 0x416, EO1EquipmentNames.GHOST_VEST, 2141, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 47
    EO1EquipmentData(EO1ItemType.Equipment, 0x417, EO1EquipmentNames.MOBIUS_ALB, 2142, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 34
    EO1EquipmentData(EO1ItemType.Equipment, 0x418, EO1EquipmentNames.ANGEL_ROBE, 2143, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 45
    EO1EquipmentData(EO1ItemType.Equipment, 0x419, EO1EquipmentNames.FAIRY_MAIL, 2144, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 47
    EO1EquipmentData(EO1ItemType.Equipment, 0x41A, EO1EquipmentNames.RUBY_MAIL, 2145, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 42
    EO1EquipmentData(EO1ItemType.Equipment, 0x41B, EO1EquipmentNames.HEX_MANTLE, 2146, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 34
    EO1EquipmentData(EO1ItemType.Equipment, 0x41C, EO1EquipmentNames.MOSS_COAT, 2147, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 35
    EO1EquipmentData(EO1ItemType.Equipment, 0x41D, EO1EquipmentNames.FLAME_COAT, 2148, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 40
    EO1EquipmentData(EO1ItemType.Equipment, 0x41E, EO1EquipmentNames.FROST_COAT, 2149, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 40
    EO1EquipmentData(EO1ItemType.Equipment, 0x41F, EO1EquipmentNames.VOLT_COAT, 2150, EO1EquipmentType.Armor), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 40
]

SHIELD_DATA: list[EO1EquipmentData] = [
    EO1EquipmentData(EO1ItemType.Equipment, 0x7F6, EO1EquipmentNames.TARGE, 2151, EO1EquipmentType.Shield), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0x7F7, EO1EquipmentNames.HIDE_ASPIS, 2152, EO1EquipmentType.Shield), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 2
    EO1EquipmentData(EO1ItemType.Equipment, 0x7F8, EO1EquipmentNames.ASPIS, 2153, EO1EquipmentType.Shield), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 2
    EO1EquipmentData(EO1ItemType.Equipment, 0x7F9, EO1EquipmentNames.OVAL_ASPIS, 2154, EO1EquipmentType.Shield), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 5
    EO1EquipmentData(EO1ItemType.Equipment, 0x7FA, EO1EquipmentNames.HEAT_ASPIS, 2155, EO1EquipmentType.Shield), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 10
    EO1EquipmentData(EO1ItemType.Equipment, 0x7FB, EO1EquipmentNames.GUM_ASPIS, 2156, EO1EquipmentType.Shield), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 7
    EO1EquipmentData(EO1ItemType.Equipment, 0x7FC, EO1EquipmentNames.BODY_ASPIS, 2157, EO1EquipmentType.Shield), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 14
    EO1EquipmentData(EO1ItemType.Equipment, 0x7FD, EO1EquipmentNames.EBON_ASPIS, 2158, EO1EquipmentType.Shield), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 10
    EO1EquipmentData(EO1ItemType.Equipment, 0x7FE, EO1EquipmentNames.MOON_ASPIS, 2159, EO1EquipmentType.Shield), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 20
    EO1EquipmentData(EO1ItemType.Equipment, 0x7FF, EO1EquipmentNames.KING_ASPIS, 2160, EO1EquipmentType.Shield), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 14
    EO1EquipmentData(EO1ItemType.Equipment, 0x800, EO1EquipmentNames.HALO_ASPIS, 2161, EO1EquipmentType.Shield), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 28
    EO1EquipmentData(EO1ItemType.Equipment, 0x801, EO1EquipmentNames.HOLY_ASPIS, 2162, EO1EquipmentType.Shield), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 32
    EO1EquipmentData(EO1ItemType.Equipment, 0x802, EO1EquipmentNames.PAIN_ASPIS, 2163, EO1EquipmentType.Shield), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 60
]

HEADGEAR_DATA: list[EO1EquipmentData] = [
    EO1EquipmentData(EO1ItemType.Equipment, 0x7D1, EO1EquipmentNames.HAIRPIN, 2164, EO1EquipmentType.Headgear), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0x7D2, EO1EquipmentNames.HIDE_HAT, 2165, EO1EquipmentType.Headgear), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0x7D3, EO1EquipmentNames.PLUMED_HAT, 2166, EO1EquipmentType.Headgear), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 2
    EO1EquipmentData(EO1ItemType.Equipment, 0x7D4, EO1EquipmentNames.CHAIN_HELM, 2167, EO1EquipmentType.Headgear), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 3
    EO1EquipmentData(EO1ItemType.Equipment, 0x7D5, EO1EquipmentNames.GUM_HELM, 2168, EO1EquipmentType.Headgear), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 3
    EO1EquipmentData(EO1ItemType.Equipment, 0x7D6, EO1EquipmentNames.SCALE_HELM, 2169, EO1EquipmentType.Headgear), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 4
    EO1EquipmentData(EO1ItemType.Equipment, 0x7D7, EO1EquipmentNames.SCALE_CAP, 2170, EO1EquipmentType.Headgear), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 6
    EO1EquipmentData(EO1ItemType.Equipment, 0x7D8, EO1EquipmentNames.SANDY_PIN, 2171, EO1EquipmentType.Headgear), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 4
    EO1EquipmentData(EO1ItemType.Equipment, 0x7D9, EO1EquipmentNames.TIGER_CAP, 2172, EO1EquipmentType.Headgear), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 7
    EO1EquipmentData(EO1ItemType.Equipment, 0x7DA, EO1EquipmentNames.CIRCLET, 2173, EO1EquipmentType.Headgear), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 5
    EO1EquipmentData(EO1ItemType.Equipment, 0x7DB, EO1EquipmentNames.BLOOD_HELM, 2174, EO1EquipmentType.Headgear), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 8
    EO1EquipmentData(EO1ItemType.Equipment, 0x7DC, EO1EquipmentNames.ANGEL_HELM, 2175, EO1EquipmentType.Headgear), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 10
]

GLOVES_DATA: list[EO1EquipmentData] = [
    EO1EquipmentData(EO1ItemType.Equipment, 0x7E2, EO1EquipmentNames.KNIT_GLOVE, 2176, EO1EquipmentType.Gloves), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0x7E3, EO1EquipmentNames.HIDE_GLOVE, 2177, EO1EquipmentType.Gloves), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0x7E4, EO1EquipmentNames.DOWN_GLOVE, 2178, EO1EquipmentType.Gloves), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 2
    EO1EquipmentData(EO1ItemType.Equipment, 0x7E5, EO1EquipmentNames.IRON_GLOVE, 2179, EO1EquipmentType.Gloves), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 3
    EO1EquipmentData(EO1ItemType.Equipment, 0x7E6, EO1EquipmentNames.BEAR_GLOVE, 2180, EO1EquipmentType.Gloves), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 3
    EO1EquipmentData(EO1ItemType.Equipment, 0x7E7, EO1EquipmentNames.GUM_GLOVE, 2181, EO1EquipmentType.Gloves), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 3
    EO1EquipmentData(EO1ItemType.Equipment, 0x7E8, EO1EquipmentNames.FANG_GLOVE, 2182, EO1EquipmentType.Gloves), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 4
    EO1EquipmentData(EO1ItemType.Equipment, 0x7E9, EO1EquipmentNames.SAND_GLOVE, 2183, EO1EquipmentType.Gloves), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 4
    EO1EquipmentData(EO1ItemType.Equipment, 0x7EA, EO1EquipmentNames.TIGER_HAND, 2184, EO1EquipmentType.Gloves), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 6
    EO1EquipmentData(EO1ItemType.Equipment, 0x7EB, EO1EquipmentNames.RUNE_GLOVE, 2185, EO1EquipmentType.Gloves), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 5
    EO1EquipmentData(EO1ItemType.Equipment, 0x7EC, EO1EquipmentNames.BLOOD_GAGE, 2186, EO1EquipmentType.Gloves), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 8
    EO1EquipmentData(EO1ItemType.Equipment, 0x7ED, EO1EquipmentNames.BRAVE_GAGE, 2187, EO1EquipmentType.Gloves), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 11
    EO1EquipmentData(EO1ItemType.Equipment, 0x7EE, EO1EquipmentNames.EBON_GLOVE, 2188, EO1EquipmentType.Gloves), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 9
    EO1EquipmentData(EO1ItemType.Equipment, 0x7EF, EO1EquipmentNames.ATHANOR, 2189, EO1EquipmentType.Gloves), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 7
    EO1EquipmentData(EO1ItemType.Equipment, 0x7F0, EO1EquipmentNames.RUBY_GAGE, 2190, EO1EquipmentType.Gloves), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 10
    EO1EquipmentData(EO1ItemType.Equipment, 0x7F1, EO1EquipmentNames.TOXIC_GAGE, 2191, EO1EquipmentType.Gloves), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 2
]

BOOTS_DATA: list[EO1EquipmentData] = [
    EO1EquipmentData(EO1ItemType.Equipment, 0x808, EO1EquipmentNames.LEAF_BOOT, 2192, EO1EquipmentType.Boots), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0x809, EO1EquipmentNames.HIDE_BOOT, 2193, EO1EquipmentType.Boots), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0x80A, EO1EquipmentNames.PLUME_BOOT, 2194, EO1EquipmentType.Boots), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 2
    EO1EquipmentData(EO1ItemType.Equipment, 0x80B, EO1EquipmentNames.CHAIN_BOOT, 2195, EO1EquipmentType.Boots), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 3
    EO1EquipmentData(EO1ItemType.Equipment, 0x80C, EO1EquipmentNames.MOCCASINS, 2196, EO1EquipmentType.Boots), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 3
    EO1EquipmentData(EO1ItemType.Equipment, 0x80D, EO1EquipmentNames.SCALE_BOOT, 2197, EO1EquipmentType.Boots), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 4
    EO1EquipmentData(EO1ItemType.Equipment, 0x80E, EO1EquipmentNames.FAIRY_BOOT, 2198, EO1EquipmentType.Boots), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 4
    EO1EquipmentData(EO1ItemType.Equipment, 0x80F, EO1EquipmentNames.TIGER_BOOT, 2199, EO1EquipmentType.Boots), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 6
    EO1EquipmentData(EO1ItemType.Equipment, 0x810, EO1EquipmentNames.FLAME_BOOT, 2200, EO1EquipmentType.Boots), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 6
    EO1EquipmentData(EO1ItemType.Equipment, 0x811, EO1EquipmentNames.FUR_BOOT, 2201, EO1EquipmentType.Boots), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 7
    EO1EquipmentData(EO1ItemType.Equipment, 0x812, EO1EquipmentNames.DYED_BOOT, 2202, EO1EquipmentType.Boots), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 8
    EO1EquipmentData(EO1ItemType.Equipment, 0x813, EO1EquipmentNames.SPEED_BOOT, 2203, EO1EquipmentType.Boots), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 12
]

ACCESSORY_DATA: list[EO1EquipmentData] = [
    EO1EquipmentData(EO1ItemType.Equipment, 0xBB9, EO1EquipmentNames.HIDE_BELT, 2204, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0xBBA, EO1EquipmentNames.HIDE_RING, 2205, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0xBBB, EO1EquipmentNames.RED_CHARM, 2206, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0xBBC, EO1EquipmentNames.PETAL_RING, 2207, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0xBBD, EO1EquipmentNames.CUT_CHARM, 2208, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 2
    EO1EquipmentData(EO1ItemType.Equipment, 0xBBE, EO1EquipmentNames.GEM_RING, 2209, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0xBBF, EO1EquipmentNames.LEAF_CAPE, 2210, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 2
    EO1EquipmentData(EO1ItemType.Equipment, 0xBC0, EO1EquipmentNames.FIRE_RING, 2211, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0xBC1, EO1EquipmentNames.STAR_CHARM, 2212, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0xBC2, EO1EquipmentNames.TUSK_CHARM, 2213, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0xBC3, EO1EquipmentNames.OLD_CHOKER, 2214, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0xBC4, EO1EquipmentNames.HIDE_CAPE, 2215, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 2
    EO1EquipmentData(EO1ItemType.Equipment, 0xBC5, EO1EquipmentNames.AMBER_RING, 2216, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0xBC6, EO1EquipmentNames.SEA_CHARM, 2217, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0xBC7, EO1EquipmentNames.BLUE_RING, 2218, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0xBC8, EO1EquipmentNames.RED_CAPE, 2219, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 2
    EO1EquipmentData(EO1ItemType.Equipment, 0xBC9, EO1EquipmentNames.EVIL_CHARM, 2220, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0xBCA, EO1EquipmentNames.ROSE_RING, 2221, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0xBCB, EO1EquipmentNames.ROYAL_RING, 2222, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 1
    EO1EquipmentData(EO1ItemType.Equipment, 0xBCC, EO1EquipmentNames.GOLD_CAPE, 2223, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 3
    EO1EquipmentData(EO1ItemType.Equipment, 0xBCD, EO1EquipmentNames.ANGEL_RING, 2224, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 2
    EO1EquipmentData(EO1ItemType.Equipment, 0xBCE, EO1EquipmentNames.WARD_GEM, 2225, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 2
    EO1EquipmentData(EO1ItemType.Equipment, 0xBCF, EO1EquipmentNames.JEWEL_EYE, 2226, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 2
    EO1EquipmentData(EO1ItemType.Equipment, 0xBD0, EO1EquipmentNames.RUBY, 2227, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 4
    EO1EquipmentData(EO1ItemType.Equipment, 0xBD1, EO1EquipmentNames.SAPPHIRE, 2228, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 4
    EO1EquipmentData(EO1ItemType.Equipment, 0xBD2, EO1EquipmentNames.TOPAZ, 2229, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 4
    EO1EquipmentData(EO1ItemType.Equipment, 0xBD3, EO1EquipmentNames.TOURMALINE, 2230, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 6
    EO1EquipmentData(EO1ItemType.Equipment, 0xBD4, EO1EquipmentNames.ADAMAS, 2231, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 6
    EO1EquipmentData(EO1ItemType.Equipment, 0xBD5, EO1EquipmentNames.HEX_DOLL, 2232, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 7
    EO1EquipmentData(EO1ItemType.Equipment, 0xBD6, EO1EquipmentNames.OCARINA, 2233, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0xBD7, EO1EquipmentNames.LUTE, 2234, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0xBD8, EO1EquipmentNames.FLUTE, 2235, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0xBD9, EO1EquipmentNames.KITHARA, 2236, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0xBDA, EO1EquipmentNames.AULOS, 2237, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0xBDB, EO1EquipmentNames.ANGEL_HARP, 2238, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0xBDC, EO1EquipmentNames.SYRINX, 2239, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0xBDD, EO1EquipmentNames.TOWN_MEDAL, 2240, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0xBDE, EO1EquipmentNames.TOWN_CROWN, 2241, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0xBDF, EO1EquipmentNames.MOSS_RING, 2242, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 0
    EO1EquipmentData(EO1ItemType.Equipment, 0xBE0, EO1EquipmentNames.MOSS_BAND, 2243, EO1EquipmentType.Accessory), # DmgType: Slash, Secondary DmgType: Slash, ATK: 0, DEF: 0
]

ALL_EQUIPMENT_DATA: list[EO1EquipmentData] = [
    *SWORD_DATA,
    *STAFF_DATA,
    *AXE_DATA,
    *KATANA_DATA,
    *BOW_DATA,
    *WHIP_DATA,
    *ARMOR_DATA,
    *SHIELD_DATA,
    *HEADGEAR_DATA,
    *GLOVES_DATA,
    *BOOTS_DATA,
    *ACCESSORY_DATA
]

ALL_ITEM_DATA: list[EO1ItemData] = [
    *CONSUMABLE_DATA,
    *KEY_ITEM_DATA,
    *QUEST_ITEM_DATA,
    *ALL_EQUIPMENT_DATA
]

ITEM_PER_AP_ITEM_ID: dict[int, EO1ItemData] = {item_data.ap_item_id:item_data for item_data in ALL_ITEM_DATA}
ITEM_PER_EO1_ID: dict[int, EO1ItemData] = {item_data.item_id:item_data for item_data in ALL_ITEM_DATA}
ITEM_PER_NAME: dict[str, EO1ItemData] = {item_data.name:item_data for item_data in ALL_ITEM_DATA}

# These are for the client.
KEY_ITEMS_WITH_FLAG: list[EO1KeyItem] = [key_item_data for key_item_data in KEY_ITEM_DATA if key_item_data.associated_flag != 0]
KEY_ITEM_DATA_BY_ITEM_ID: dict[int, EO1KeyItem] = {key_item_data.item_id:key_item_data for key_item_data in KEY_ITEMS_WITH_FLAG}