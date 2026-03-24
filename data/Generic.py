from enum import IntEnum

class EO1Ailment(IntEnum):
    NONE = 0
    HEAD_BIND = 1
    ARM_BIND = 2
    LEG_BIND = 3
    INSTANT_DEATH = 4
    PETRIFY = 5
    SLEEP = 6
    PARALYSIS = 7
    CONFUSION = 8
    FEAR = 9
    POISON = 10
    BLIND = 11
    CURSE = 12
    STUN = 13

class EO1Element(IntEnum):
    NONE = 0
    SLASH = 1
    BASH = 2
    STAB = 3
    FIRE = 4
    ICE = 5
    THUNDER = 6
    PHYSICAL = 7
    ELEMENTAL = 8
    #ALL = 9