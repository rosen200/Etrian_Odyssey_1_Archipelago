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
