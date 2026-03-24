from ..data.EnemyData import *
from .LogicData import *

class ConditionalDropProcessor:
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
