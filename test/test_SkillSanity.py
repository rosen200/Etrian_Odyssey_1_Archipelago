from .Bases import EtrianOdysseyTestBase
from .Constant import *
from ..Constant import *
from ..Options import *


BASE_OPTIONS = {
    **OptionSets.DEFAULT_NO_BATTLE_LOGIC,
    **OptionSets.NO_LEVEL_SHUFFLING,
    **OptionSets.NO_FLOOR_SHUFFLING,
    **OptionSets.NO_CLASS_SHUFFLING,
}


class SkillSanityIndividualShuffleTest(EtrianOdysseyTestBase):
    options = {
        OptionKeys.GOAL: EO1Goal.defeat_etreant.value,
        **BASE_OPTIONS,
        **OptionSets.ENABLE_ALL_LOCATIONS, # Individual Shuffling need more locations.

        # Skills
        OptionKeys.SKILL_SANITY_MODE: SkillSanityType.shuffle_individually.value,
        OptionKeys.SHUFFLE_GENERIC_STATS_INCREASE_SKILLS: False,
        OptionKeys.SHUFFLE_GATHERING_SKILLS: False,
    }

class SkillSanityAllIndividualShuffleTest(EtrianOdysseyTestBase):
    options = {
        OptionKeys.GOAL: EO1Goal.defeat_etreant.value,
        **BASE_OPTIONS,
        **OptionSets.ENABLE_ALL_LOCATIONS,  # Individual Shuffling need more locations.

        # Skills
        OptionKeys.SKILL_SANITY_MODE: SkillSanityType.shuffle_individually.value,
        OptionKeys.SHUFFLE_GENERIC_STATS_INCREASE_SKILLS: True,
        OptionKeys.SHUFFLE_GATHERING_SKILLS: True,
    }

class SkillSanityGroupShuffleTest(EtrianOdysseyTestBase):
    options = {
        OptionKeys.GOAL: EO1Goal.defeat_etreant.value,
        **BASE_OPTIONS,
        **OptionSets.DISABLE_ALL_OPTIONAL_LOCATIONS,

        # Skills
        OptionKeys.SKILL_SANITY_MODE: SkillSanityType.shuffle_group.value,
        OptionKeys.SHUFFLE_GENERIC_STATS_INCREASE_SKILLS: False,
        OptionKeys.SHUFFLE_GATHERING_SKILLS: False,
    }

class SkillSanityAllGroupShuffleTest(EtrianOdysseyTestBase):
    options = {
        OptionKeys.GOAL: EO1Goal.defeat_etreant.value,
        **BASE_OPTIONS,
        **OptionSets.DISABLE_ALL_OPTIONAL_LOCATIONS,

        # Skills
        OptionKeys.SKILL_SANITY_MODE: SkillSanityType.shuffle_group.value,
        OptionKeys.SHUFFLE_GENERIC_STATS_INCREASE_SKILLS: True,
        OptionKeys.SHUFFLE_GATHERING_SKILLS: True,
    }

class SkillSanityNoSkillsRequirementsTest(EtrianOdysseyTestBase):
    options = {
        OptionKeys.GOAL: EO1Goal.defeat_etreant.value,
        **BASE_OPTIONS,
        **OptionSets.ENABLE_ALL_LOCATIONS,  # Individual Shuffling need more locations.

        # Skills
        OptionKeys.SKILL_SANITY_MODE: SkillSanityType.shuffle_individually.value,
        OptionKeys.REMOVE_SKILLS_REQUIREMENTS: True,
        OptionKeys.SHUFFLE_GENERIC_STATS_INCREASE_SKILLS: True,
        OptionKeys.SHUFFLE_GATHERING_SKILLS: True,
    }