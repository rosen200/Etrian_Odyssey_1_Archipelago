from __future__ import annotations
from typing import TYPE_CHECKING, Callable, cast
from abc import ABC, abstractmethod
from ..LogicData import *

from BaseClasses import CollectionState

from ...data.EnemyData import *
from ..SingleEnemyBattleProcessor import *
from .SimplifiedClassValues import *
from .SimplifiedEnemyValues import *
from .SimplifiedSkillValues import *
from .SimplifiedValuesCriteria import *

class SimplifiedSingleEnemyBattleProcessor(SingleEnemyBattleProcessor):
    def __level_requirement_met(self, enemy_data: EnemyData, logic_data: AllLogicData) -> bool:
        # For now, just use the raw level.
        effective_enemy_level = enemy_data.level
        return logic_data.current_level_cap >= max(1, effective_enemy_level)

    def __evaluate_or_criteria(self, criteria: OrSVCriteria, class_logic_data: list[SingleClassLogicData]) -> bool:
        for inner_criteria in criteria.criteria:
            if self.__condition_is_met(inner_criteria, class_logic_data):
                return True
        return False

    def __evaluate_and_criteria(self, criteria: AndSVCriteria, class_logic_data: list[SingleClassLogicData]) -> bool:
        for inner_criteria in criteria.criteria:
            if not self.__condition_is_met(inner_criteria, class_logic_data):
                return False
        return True

    def __evaluate_true_criteria(self, criteria: TrueSVCriteria, class_logic_data: list[SingleClassLogicData]) -> bool:
        return True

    def __evaluate_class_criteria(self, criteria: ClassSVCriteria, class_logic_data: list[SingleClassLogicData]) -> bool:
        front_row_count = 0
        back_row_count = 0
        total_count = 0

        for class_data in class_logic_data:
            if not class_data.class_unlocked:
                continue

            simplified_class_data = SIMPLIFIED_CLASS_VALUES_BY_NAME[class_data.class_name]

            if not self.__condition_is_met(criteria.criteria, [class_data]):
                continue

            if simplified_class_data.is_front_row_viable:
                front_row_count += 1
            if simplified_class_data.is_back_row_viable:
                back_row_count += 1
            total_count += 1

        if criteria.front_class_count is not None:
            if front_row_count < criteria.front_class_count:
                return False

        if criteria.back_class_count is not None:
            if back_row_count < criteria.back_class_count:
                return False

        if criteria.total_class_count is not None:
            if total_count < criteria.total_class_count:
                return False

        return True

    def __evaluate_dmg_skill_criteria(self, criteria: CanUseDmgSkillSVCriteria, class_logic_data: list[SingleClassLogicData]) -> bool:
        #for class_data in logic_data.class_data.class_as_list:
        #    pass
        #for class_data in logic_data.class_data.class_as_list:


        return False

    def __evaluate_anti_status_criteria(self, criteria: HasAntiStatusSVCriteria, class_logic_data: list[SingleClassLogicData]) -> bool:
        return False

    def __evaluate_anti_bind_criteria(self, criteria: HasAntiBindSVCriteria, class_logic_data: list[SingleClassLogicData]) -> bool:
        return False

    def __evaluate_inflict_ailment_criteria(self, criteria: CanInflictAilment, class_logic_data: list[SingleClassLogicData]) -> bool:
        return False

    def __evaluate_use_active_skill_criteria(self, criteria: CanUseActiveSkill, class_logic_data: list[SingleClassLogicData]) -> bool:
        for class_data in class_logic_data:
            if self.__class_evaluate_use_active_skill_criteria(criteria, class_data):
                return True
        return False

    def __class_evaluate_use_active_skill_criteria(self, criteria: CanUseActiveSkill, class_data: SingleClassLogicData) -> bool:
        def skill_match(skill: SkillLogicData) -> bool:
            if not skill.skill_usable:
                return False

            simplified_values = SIMPLIFIED_SKILL_BY_SKILL_ID[skill.skill_id]
            if simplified_values.get_skill_use_type() != SkillUseType.ACTIVE:
                return False

            active_skill_values = cast(ActiveSkillValues, simplified_values)
            if criteria.skill_viability_level is not None:
                if active_skill_values.viability_level < criteria.skill_viability_level.value:
                    return False

            skill_data = SKILL_DATA_BY_ID[skill.skill_id]

            if active_skill_values.is_offensive_skill():
                for element in criteria.damage_type_resistances:
                    if skill_data.primary_element == element:
                        return False
                    elif skill_data.secondary_element is not None:
                        if skill_data.secondary_element == element:
                            return False

            for ailment in criteria.ailment_resistances:
                raise Exception("Ailment not supported")

            return True

        if not class_data.class_unlocked:
            return False

        match_count = 0
        for skill_logic_data in class_data.class_skills.values():
            if skill_match(skill_logic_data):
                match_count += 1

        return match_count >= criteria.skill_count

    dispatch_dict: dict[type, Callable[[SimplifiedSingleEnemyBattleProcessor, SVCriteria, list[SingleClassLogicData]], bool]] = {
        OrSVCriteria: __evaluate_or_criteria,
        AndSVCriteria: __evaluate_and_criteria,
        TrueSVCriteria: __evaluate_true_criteria,
        ClassSVCriteria: __evaluate_class_criteria,
        CanUseDmgSkillSVCriteria: __evaluate_dmg_skill_criteria,
        HasAntiStatusSVCriteria: __evaluate_anti_status_criteria,
        HasAntiBindSVCriteria: __evaluate_anti_bind_criteria,
        CanInflictAilment: __evaluate_inflict_ailment_criteria,
        CanUseActiveSkill: __evaluate_use_active_skill_criteria
    }

    def __condition_is_met(self, criteria: SVCriteria, class_logic_data: list[SingleClassLogicData]) -> bool:
        return self.dispatch_dict[type(criteria)](self, criteria, class_logic_data)

    def can_survive_enemy(self, enemy_id: int, state: CollectionState, logic_data: AllLogicData) -> bool:
        enemy_data = self.get_enemy_data(enemy_id)
        if not self.__level_requirement_met(enemy_data, logic_data):
            return False

        # TODO Temporary
        if enemy_id not in SIMPLIFIED_ENEMY_VALUES_BY_ID:
            return True

        sv_enemy = SIMPLIFIED_ENEMY_VALUES_BY_ID[enemy_id]

        # If player has more than double the level, bypass other checks.
        if enemy_data.level * 2 < logic_data.current_level_cap:
            return True

        if sv_enemy.survive_criteria is None:
            return True

        return self.__condition_is_met(sv_enemy.survive_criteria, logic_data.class_data.class_as_list)

    def can_defeat_enemy(self, enemy_id: int, state: CollectionState, logic_data: AllLogicData) -> bool:
        enemy_data = self.get_enemy_data(enemy_id)
        if not self.__level_requirement_met(enemy_data, logic_data):
            return False

        # TODO Temporary
        if enemy_id not in SIMPLIFIED_ENEMY_VALUES_BY_ID:
            return False

        sv_enemy = SIMPLIFIED_ENEMY_VALUES_BY_ID[enemy_id]

        # If player has more than double the level, bypass other checks.
        if enemy_data.level * 2 < logic_data.current_level_cap:
            return True

        if sv_enemy.defeat_criteria is None:
            return True

        return self.__condition_is_met(sv_enemy.defeat_criteria, logic_data.class_data.class_as_list)
