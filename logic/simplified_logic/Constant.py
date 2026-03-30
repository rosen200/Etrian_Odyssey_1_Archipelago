from enum import IntEnum

class SkillPower(IntEnum):
    WEAK = 1
    MEDIUM = 2
    STRONG = 3

class SkillViabilityLevel(IntEnum):
    TERRIBLE = 0 # Skills that doesn't work or do basically nothing.
    SITUATIONAL = 0 # Skills that are Normal or Good, but are situational.
    BAD = 1
    NORMAL = 2
    GOOD = 3

# This is almost a 1:1 copy from EO1SkilLEffect except for the last few. They could be merged.
class SkillEffectType(IntEnum):
    ATTACK = 0
    DEFENSE = 1
    SPEED = 2
    ACCURACY = 3
    EVASION = 4
    HP_RECOVERY = 5
    STANCE = 6
    AFFINITY = 7
    MAXHP = 8
    ELEMENTAL_DEFENSE = 9
    SP_RECOVERY = 10
    AILMENT_RECOVERY = 11

# This is a simplified version of EO1SkillTarget.
class SkillTargetType(IntEnum):
    SINGLE = 1
    ALL = 2
    SELF = 3
    FRONT_ALL = 4
    BACK_ALL = 5