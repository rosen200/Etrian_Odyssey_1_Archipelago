from ..data.EnemyData import *
from .LogicData import *

class ConditionalDropProcessor:
    def __is_conditional_ignorable_for_regular_drops(self, drop_condition: DropCondition) -> bool:
        if (drop_condition == DropCondition.NONE or
            drop_condition == DropCondition.KILL_1_TURNS or
            drop_condition == DropCondition.KILL_2_TURNS or
            drop_condition == DropCondition.KILL_3_TURNS or
            drop_condition == DropCondition.KILL_7_TURNS or
            drop_condition == DropCondition.FULL_BIND or
            drop_condition == DropCondition.INSTANT_DEATH): # Instant death is never considered to proc in logic.
            return True
        if (drop_condition == DropCondition.STAB or
            drop_condition == DropCondition.FIRE or
            drop_condition == DropCondition.ICE or
            drop_condition == DropCondition.NOT_BASH or
            drop_condition == DropCondition.NOT_STAB or
            drop_condition == DropCondition.NOT_PHYSICAL or
            drop_condition == DropCondition.NOT_FIRE):
            return False
        raise Exception(f"Unknown drop_condition: {drop_condition}")

    def can_defeat_without_fulfilling_drop_condition(self, enemy_id: int, logic_data: AllLogicData) -> bool:
        enemy_data = ENEMY_BY_ID[enemy_id]

        # If the conditional drop isn't a guaranteed drop override, ignore everything else.
        if enemy_data.item_3_drop_chance < 100:
            return True

        if self.__is_conditional_ignorable_for_regular_drops(enemy_data.drop_condition):
            return True

        # TODO temporary.
        if enemy_id == EO1Enemies.FIREBIRD:
            return True

        raise Exception(f"enemy {enemy_id}")

    def can_fulfill_drop_condition(self, enemy_id: int, logic_data: AllLogicData) -> bool:
        enemy_data = ENEMY_BY_ID[enemy_id]

        if enemy_data.drop_condition == DropCondition.STAB:
            return False
        if enemy_data.drop_condition == DropCondition.FIRE:
            return False
        if enemy_data.drop_condition == DropCondition.ICE:
            return False
        if enemy_data.drop_condition == DropCondition.NOT_BASH:
            return False
        if enemy_data.drop_condition == DropCondition.NOT_STAB:
            return False
        if enemy_data.drop_condition == DropCondition.NOT_PHYSICAL:
            return False
        if enemy_data.drop_condition == DropCondition.NOT_FIRE:
            return False
        if enemy_data.drop_condition == DropCondition.INSTANT_DEATH:
            return False
        if enemy_data.drop_condition == DropCondition.FULL_BIND:
            return False
        if enemy_data.drop_condition == DropCondition.KILL_1_TURNS:
            return False
        if enemy_data.drop_condition == DropCondition.KILL_2_TURNS:
            return False
        if enemy_data.drop_condition == DropCondition.KILL_3_TURNS:
            return False
        if enemy_data.drop_condition == DropCondition.KILL_7_TURNS:
            return False
        if enemy_data.drop_condition == DropCondition.NONE:
            return True
        raise Exception(f"Unknown drop condition {enemy_data.drop_condition}.")
