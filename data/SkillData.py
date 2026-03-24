from typing import TYPE_CHECKING, NamedTuple, Optional
from enum import IntEnum
from dataclasses import dataclass

from .Generic import *

class EO1Skills:
    LANDSKNECHT_HP_UP = 0x01
    LANDSKNECHT_TP_UP = 0x02
    LANDSKNECHT_ATK_UP = 0x03
    LANDSKNECHT_DEF_UP = 0x04
    LANDSKNECHT_AXES = 0x05
    LANDSKNECHT_SWORDS = 0x06
    LANDSKNECHT_2_HIT = 0x07
    LANDSKNECHT_MINE = 0x08
    LANDSKNECHT_WAR_CRY = 0x09
    LANDSKNECHT_HELL_CRY = 0x0A
    LANDSKNECHT_ARM_HEAL = 0x0B
    LANDSKNECHT_CRUSH = 0x0C
    LANDSKNECHT_STUNNER = 0x0D
    LANDSKNECHT_SILENCER = 0x0E
    LANDSKNECHT_CLEAVER = 0x0F
    LANDSKNECHT_TORNADO = 0x10
    LANDSKNECHT_ALLSLASH = 0x11
    LANDSKNECHT_BLAZER = 0x12
    LANDSKNECHT_SHOCKER = 0x13
    LANDSKNECHT_FREEZER = 0x14
    LANDSKNECHT_FLEE = 0x15
    SURVIVALIST_HP_UP = 0x16
    SURVIVALIST_TP_UP = 0x17
    SURVIVALIST_AGI_UP = 0x18
    SURVIVALIST_BOWS = 0x19
    SURVIVALIST_1ST_HIT = 0x1A
    SURVIVALIST_AMBUSH = 0x1B
    SURVIVALIST_CHOP = 0x1C
    SURVIVALIST_MINE = 0x1D
    SURVIVALIST_TAKE = 0x1E
    SURVIVALIST_1ST_TURN = 0x1F
    SURVIVALIST_TRICKERY = 0x20
    SURVIVALIST_QUICKEN = 0x21
    SURVIVALIST_TRUESHOT = 0x22
    SURVIVALIST_MULTIHIT = 0x23
    SURVIVALIST_DISABLE = 0x24
    SURVIVALIST_APOLLON = 0x25
    SURVIVALIST_CLOAK = 0x26
    SURVIVALIST_ESCAPE = 0x27
    SURVIVALIST_AWARE = 0x28
    SURVIVALIST_STALKER = 0x29
    SURVIVALIST_OWL_EYE = 0x2A
    PROTECTOR_HP_UP = 0x2B
    PROTECTOR_TP_UP = 0x2C
    PROTECTOR_DEF_UP = 0x2D
    PROTECTOR_SHIELDS = 0x2E
    PROTECTOR_AEGIS = 0x2F
    PROTECTOR_EN_GARDE = 0x30
    PROTECTOR_MINE = 0x31
    PROTECTOR_PROVOKE = 0x32
    PROTECTOR_F_GUARD = 0x33
    PROTECTOR_B_GUARD = 0x34
    PROTECTOR_PARRY = 0x35
    PROTECTOR_FORTIFY = 0x36
    PROTECTOR_DEFENDER = 0x37
    PROTECTOR_SMITE = 0x38
    PROTECTOR_ANTIFIRE = 0x39
    PROTECTOR_ANTIVOLT = 0x3A
    PROTECTOR_ANTICOLD = 0x3B
    PROTECTOR_CURE = 0x3C
    PROTECTOR_CURE_II = 0x3D
    PROTECTOR_FLEE = 0x3E
    PROTECTOR_STALKER = 0x3F
    DARK_HUNTER_HP_UP = 0x40
    DARK_HUNTER_TP_UP = 0x41
    DARK_HUNTER_ATK_UP = 0x42
    DARK_HUNTER_WHIPS = 0x43
    DARK_HUNTER_SWORDS = 0x44
    DARK_HUNTER_BOOST_UP = 0x45
    DARK_HUNTER_FURY = 0x46
    DARK_HUNTER_TAKE = 0x47
    DARK_HUNTER_CLOAK = 0x48
    DARK_HUNTER_VIPER = 0x49
    DARK_HUNTER_GAG = 0x4A
    DARK_HUNTER_CUFFS = 0x4B
    DARK_HUNTER_SHACKLES = 0x4C
    DARK_HUNTER_ECSTASY = 0x4D
    DARK_HUNTER_CLIMAX = 0x4E
    DARK_HUNTER_HYPNOS = 0x4F
    DARK_HUNTER_NERVE = 0x50
    DARK_HUNTER_PETRIFY = 0x51
    DARK_HUNTER_BAIT = 0x52
    DARK_HUNTER_DRAIN = 0x53
    DARK_HUNTER_MIRAGE = 0x54
    RONIN_HP_UP = 0x55
    RONIN_TP_UP = 0x56
    RONIN_ATK_UP = 0x57
    RONIN_KATANAS = 0x58
    RONIN_CRIT_UP = 0x59
    RONIN_SIGHT = 0x5A
    RONIN_MINE = 0x5B
    RONIN_IBUKI = 0x5C
    RONIN_KESAGIRI = 0x5D
    RONIN_OVERHEAD = 0x5E
    RONIN_ZAMBA = 0x5F
    RONIN_MIDAREBA = 0x60
    RONIN_OROCHI = 0x61
    RONIN_SEIGAN = 0x62
    RONIN_MIKIRI = 0x63
    RONIN_KOTEUCHI = 0x64
    RONIN_RAIZUKI = 0x65
    RONIN_IAI = 0x66
    RONIN_KUBIUCHI = 0x67
    RONIN_GATOTSU = 0x68
    RONIN_HYOSETSU = 0x69
    MEDIC_HP_UP = 0x6A
    MEDIC_TP_UP = 0x6B
    MEDIC_ATK_UP = 0x6C
    MEDIC_HEALER = 0x6D
    MEDIC_PATCH_UP = 0x6E
    MEDIC_SCAVENGE = 0x6F
    MEDIC_TP_REGEN = 0x70
    MEDIC_CHOP = 0x71
    MEDIC_CURE = 0x72
    MEDIC_CURE_II = 0x73
    MEDIC_CURE_III = 0x74
    MEDIC_SALVE = 0x75
    MEDIC_SALVE_II = 0x76
    MEDIC_REVIVE = 0x77
    MEDIC_UNBIND = 0x78
    MEDIC_REFRESH = 0x79
    MEDIC_IMMUNIZE = 0x7A
    MEDIC_CADUCEUS = 0x7B
    MEDIC_CPR = 0x7C
    MEDIC_REGEN = 0x7D
    MEDIC_H_TOUCH = 0x7E
    ALCHEMIST_TP_UP = 0x7F
    ALCHEMIST_FIRE_UP = 0x80
    ALCHEMIST_ICE_UP = 0x81
    ALCHEMIST_VOLT_UP = 0x82
    ALCHEMIST_TOXINS = 0x83
    ALCHEMIST_SCAVENGE = 0x84
    ALCHEMIST_TP_REGEN = 0x85
    ALCHEMIST_CHOP = 0x86
    ALCHEMIST_FIRE = 0x87
    ALCHEMIST_FLAME = 0x88
    ALCHEMIST_INFERNO = 0x89
    ALCHEMIST_ICE = 0x8A
    ALCHEMIST_FREEZE = 0x8B
    ALCHEMIST_COCYTUS = 0x8C
    ALCHEMIST_VOLT = 0x8D
    ALCHEMIST_THUNDER = 0x8E
    ALCHEMIST_THOR = 0x8F
    ALCHEMIST_POISON = 0x90
    ALCHEMIST_VENOM = 0x91
    ALCHEMIST_SIGHT = 0x92
    ALCHEMIST_WARP = 0x93
    TROUBADOUR_HP_UP = 0x94
    TROUBADOUR_TP_UP = 0x95
    TROUBADOUR_SONGS = 0x96
    TROUBADOUR_DIVINITY = 0x97
    TROUBADOUR_BRAVERY = 0x98
    TROUBADOUR_SHELTER = 0x99
    TROUBADOUR_MERCURY = 0x9A
    TROUBADOUR_BLAZE = 0x9B
    TROUBADOUR_FROST = 0x9C
    TROUBADOUR_SHOCK = 0x9D
    TROUBADOUR_ERASURE = 0x9E
    TROUBADOUR_STAMINA = 0x9F
    TROUBADOUR_IFRIT = 0xA0
    TROUBADOUR_YMIR = 0xA1
    TROUBADOUR_TARANIS = 0xA2
    TROUBADOUR_HEALING = 0xA3
    TROUBADOUR_RELAXING = 0xA4
    TROUBADOUR_RECOVERY = 0xA5
    TROUBADOUR_STALKER = 0xA6
    TROUBADOUR_RETURN = 0xA7
    TROUBADOUR_TAKE = 0xA8
    HEXER_HP_UP = 0xA9
    HEXER_TP_UP = 0xAA
    HEXER_CURSES = 0xAB
    HEXER_STAGGER = 0xAC
    HEXER_MINE = 0xAD
    HEXER_SAPPING = 0xAE
    HEXER_FRAILTY = 0xAF
    HEXER_LEADEN = 0xB0
    HEXER_RELAPSE = 0xB1
    HEXER_CRANIAL = 0xB2
    HEXER_ABDOMEN = 0xB3
    HEXER_IMMOBILE = 0xB4
    HEXER_BLINDING = 0xB5
    HEXER_TORPOR = 0xB6
    HEXER_CORRUPT = 0xB7
    HEXER_EVIL_EYE = 0xB8
    HEXER_SUICIDE = 0xB9
    HEXER_BETRAYAL = 0xBA
    HEXER_PARALYZE = 0xBB
    HEXER_REVENGE = 0xBC
    HEXER_LURE = 0xBD

class EO1SkillType(IntEnum):
    PASSIVE = 0
    MASTERY = 1
    PHYSICAL_ATTACK = 2
    MAGICAL_ATTACK = 3
    AILMENT_ATTACK = 4
    DEBUFF = 5
    BUFF = 6
    COUNTER = 7
    CHASE = 8
    DEFENSE = 9
    HEAL = 10
    AILMENT_HEAL = 11
    BUFF_REMOVAL = 12
    GATHERING = 13
    SPECIAL = 14

class EO1SkillUsage(IntEnum):
    NONE = 0,
    TOWN = 1,
    DUNGEON = 2,
    BATTLE = 3,
    TOWN_DUNGEON = 4,
    DUNGEON_BATTLE = 5,
    ALL = 6,

class EO1SkillEffect(IntEnum):
    ATTACK = 0,
    SPEED = 1,
    AVOID = 2,
    STYLE = 3,
    DEFENCE = 4,
    RECOVER = 5,
    AFFINITY = 6,
    HPMAX = 7,
    HIT = 8,
    SQUEEZE = 9,

class EO1SkillTarget(IntEnum):
    ONE = 0,
    ALL = 1,
    ALL_RAND = 2,
    ALL_RAND_ONE_HIT = 3,
    ONE_CONVOLUTE = 4,
    SELF = 5,
    FRONT = 6,
    BACK = 7,

class EO1SkillSide(IntEnum):
    SELF = 0,
    OTHER = 1,
    ALL = 2,

class EO1SkillNeed(IntEnum):
    NONE = 0,
    HEAD = 1,
    ARM = 2,
    LEG = 3,
    ALL = 4,

class EO1SkillMastery(IntEnum):
    NONE = 0,
    AX = 1,
    SWORD = 2,
    SHOT = 3,
    SHIELD = 4,
    WHIP = 5,
    SAMURAI_SWORD = 6,
    FIRE = 7,
    ICE = 8,
    THUNDER = 9,
    BENOM = 10,
    RECOVERY = 11,
    SONG = 12,
    CURSE = 13,

class EO1SkillValueType(IntEnum):
    NONE = 0,
    CONSUMPTION_TP = 1,
    SKILL_COEFFICIENT = 2,
    SPEED = 3,
    HIT_RATE = 4,
    RATE_X1 = 5,
    RATE_X3 = 6,
    RATE_X4 = 7,
    COUNTER_RATE = 8,
    COUNTER_DEC_RATE = 9,
    RECOVERY_VALUE = 10,
    BST_RECOVERY_LEVEL = 11,
    ATTACK_NUMBER = 12,
    GET_SUCCESS_COEFFICIENT = 13,
    TURN_NUMBER = 14,
    SKILL_MASTER_COEFFICIENT = 15,
    ATTACK_BOOST_COEFFICIENT = 16,
    ROLLED_DAMAGE_COEFFICIENT = 17,
    EFFICACY_SUCCESS_RATE = 18,
    EFFICACY_SKILL_COEFFICIENT = 19,
    ATTR_ADD_ATTACK_SC = 20,
    ATTR_ATTACK_VALUE = 21,
    SC2 = 22,
    VALX1 = 23,
    PARAM_BOOST_HP = 50,
    PARAM_BOOST_TP = 51,
    PARAM_BOOST_AFFINITY_ALL = 52,
    PARAM_BOOST_AGI = 53,
    PARAM_BOOST_CRITICAL = 54,
    PARAM_BOOST_EXP = 55,
    PARAM_BOOST_BOOSTADD = 56,
    MUL_SKILL_COEFFICIENT = 100,
    MUL_AFFINITY = 101,
    MUL_DEFENSE = 102,
    MUL_PHYSICAL_ATTACK = 103,
    MUL_MAGIC_ATTACK = 104,
    MUL_HP_MAX = 105,
    MUL_HIT = 106,
    MUL_TARGET = 107,
    MUL_ACTION_SPEED = 108,
    HP_RECOVERY_RATE = 109,
    TP_RECOVERY_RATE = 110,
    BST_RECOVERY_TURN_CORRECTION = 111,
    ABSORPTION_RATE = 112,
    ESCAPE_RATE = 113,
    CHANGE_ATC_ATTR = 114,
    MUL_AFFINITY2 = 115,

@dataclass
class EO1SkillValue:
    skill_value_type: EO1SkillValueType
    value_per_level: list[int]

@dataclass
class EO1SkillData:
    id: int
    name: str
    ap_item_id: int
    class_name: str
    skill_index: int
    skill_type: EO1SkillType
    primary_element: EO1Element
    secondary_element: EO1Element
    ailment: EO1Ailment
    need: EO1SkillNeed
    mastery: EO1SkillMastery
    target: EO1SkillTarget
    side: EO1SkillSide
    usage: EO1SkillUsage
    effect: EO1SkillEffect
    skill_values: list[EO1SkillValue]

    def get_full_name(self) -> str:
        return f"{self.name} ({self.class_name})"

LANDSKNECHT_SKILLS: list[EO1SkillData] = [
    EO1SkillData(EO1Skills.LANDSKNECHT_HP_UP, "HP Up", 200, "Landsknecht", 0, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_HP,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.LANDSKNECHT_TP_UP, "TP Up", 201, "Landsknecht", 1, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_TP,[110,112,114,116,128,130,132,134,136,150])]),
    EO1SkillData(EO1Skills.LANDSKNECHT_ATK_UP, "ATK Up", 202, "Landsknecht", 2, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.ATTACK_BOOST_COEFFICIENT,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.LANDSKNECHT_DEF_UP, "DEF Up", 203, "Landsknecht", 3, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_AFFINITY_ALL,[95,94,93,92,91,90,89,88,87,85])]),
    EO1SkillData(EO1Skills.LANDSKNECHT_AXES, "Axes", 204, "Landsknecht", 4, EO1SkillType.MASTERY, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.SKILL_MASTER_COEFFICIENT,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.LANDSKNECHT_SWORDS, "Swords", 205, "Landsknecht", 5, EO1SkillType.MASTERY, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.SKILL_MASTER_COEFFICIENT,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.LANDSKNECHT_2_HIT, "2-Hit", 206, "Landsknecht", 6, EO1SkillType.PHYSICAL_ATTACK, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.RATE_X1,[10,11,12,13,16,17,18,19,20,23])]),
    EO1SkillData(EO1Skills.LANDSKNECHT_MINE, "Mine", 207, "Landsknecht", 20, EO1SkillType.GATHERING, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.GET_SUCCESS_COEFFICIENT,[100,102,104,106,110,111,112,113,114,120])]),
    EO1SkillData(EO1Skills.LANDSKNECHT_WAR_CRY, "War Cry", 208, "Landsknecht", 7, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[2,2,2,2,3,3,3,3,3,3]),EO1SkillValue(EO1SkillValueType.SPEED,[60,60,60,60,60,60,60,60,60,60]),EO1SkillValue(EO1SkillValueType.MUL_SKILL_COEFFICIENT,[110,113,116,119,125,127,129,131,133,140]),EO1SkillValue(EO1SkillValueType.MUL_AFFINITY,[120,120,120,120,120,118,116,114,112,110])]),
    EO1SkillData(EO1Skills.LANDSKNECHT_HELL_CRY, "Hell Cry", 209, "Landsknecht", 8, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[2,2,2,2,3,3,3,3,3,3]),EO1SkillValue(EO1SkillValueType.SPEED,[60,60,60,60,60,60,60,60,60,60]),EO1SkillValue(EO1SkillValueType.MUL_SKILL_COEFFICIENT,[120,123,126,129,135,137,139,141,143,150]),EO1SkillValue(EO1SkillValueType.MUL_AFFINITY,[120,120,120,120,120,118,116,114,112,110]),EO1SkillValue(EO1SkillValueType.MUL_HP_MAX,[80,80,80,80,80,82,84,86,88,90])]),
    EO1SkillData(EO1Skills.LANDSKNECHT_ARM_HEAL, "Arm Heal", 210, "Landsknecht", 9, EO1SkillType.AILMENT_HEAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[2,2,2,2,1,1,1,1,1,0]),EO1SkillValue(EO1SkillValueType.SPEED,[60,60,60,60,60,60,60,60,60,60])]),
    EO1SkillData(EO1Skills.LANDSKNECHT_CRUSH, "Crush", 211, "Landsknecht", 17, EO1SkillType.PHYSICAL_ATTACK, EO1Element.BASH, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.ARM, EO1SkillMastery.AX, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[160,165,170,175,185,187,190,193,196,210]),EO1SkillValue(EO1SkillValueType.SPEED,[50,50,50,50,50,50,50,50,50,50]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120])]),
    EO1SkillData(EO1Skills.LANDSKNECHT_STUNNER, "Stunner", 212, "Landsknecht", 18, EO1SkillType.PHYSICAL_ATTACK, EO1Element.BASH, EO1Element.NONE, EO1Ailment.STUN, EO1SkillNeed.ARM, EO1SkillMastery.AX, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[140,145,150,155,165,167,170,173,176,190]),EO1SkillValue(EO1SkillValueType.SPEED,[80,82,84,86,90,92,94,96,98,102]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[15,20,25,30,40,45,50,55,60,75])]),
    EO1SkillData(EO1Skills.LANDSKNECHT_SILENCER, "Silencer", 213, "Landsknecht", 19, EO1SkillType.PHYSICAL_ATTACK, EO1Element.BASH, EO1Element.NONE, EO1Ailment.HEAD_BIND, EO1SkillNeed.ARM, EO1SkillMastery.AX, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[130,131,132,133,134,135,136,137,138,140]),EO1SkillValue(EO1SkillValueType.SPEED,[60,60,60,60,60,60,60,60,60,60]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[20,21,22,23,29,30,31,32,33,40])]),
    EO1SkillData(EO1Skills.LANDSKNECHT_CLEAVER, "Cleaver", 214, "Landsknecht", 11, EO1SkillType.PHYSICAL_ATTACK, EO1Element.SLASH, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.ARM, EO1SkillMastery.SWORD, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[140,145,150,155,165,167,170,173,176,190]),EO1SkillValue(EO1SkillValueType.SPEED,[80,80,80,80,80,80,80,80,80,80]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120])]),
    EO1SkillData(EO1Skills.LANDSKNECHT_TORNADO, "Tornado", 215, "Landsknecht", 12, EO1SkillType.PHYSICAL_ATTACK, EO1Element.SLASH, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.ARM, EO1SkillMastery.SWORD, EO1SkillTarget.ONE_CONVOLUTE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[6,6,7,7,8,8,8,8,8,8]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[140,145,150,155,165,167,170,173,176,190]),EO1SkillValue(EO1SkillValueType.SPEED,[80,80,80,80,80,80,80,80,80,80]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120]),EO1SkillValue(EO1SkillValueType.SC2,[100,102,104,106,118,120,122,124,126,140])]),
    EO1SkillData(EO1Skills.LANDSKNECHT_ALLSLASH, "Allslash", 216, "Landsknecht", 13, EO1SkillType.PHYSICAL_ATTACK, EO1Element.SLASH, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.LEG, EO1SkillMastery.SWORD, EO1SkillTarget.ALL_RAND_ONE_HIT, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[6,6,7,7,8,8,8,8,8,8]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[140,145,150,155,165,167,170,173,176,190]),EO1SkillValue(EO1SkillValueType.SPEED,[80,80,80,80,80,80,80,80,80,80]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120]),EO1SkillValue(EO1SkillValueType.RATE_X3,[703000,703000,505000,505000,7030,7030,6040,6040,5050,5050])]),
    EO1SkillData(EO1Skills.LANDSKNECHT_BLAZER, "Blazer", 217, "Landsknecht", 14, EO1SkillType.CHASE, EO1Element.FIRE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.LEG, EO1SkillMastery.SWORD, EO1SkillTarget.ALL, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[8,8,9,9,10,10,10,10,10,10]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[140,145,150,155,165,167,170,173,176,190]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[200,200,200,200,200,200,200,200,200,200])]),
    EO1SkillData(EO1Skills.LANDSKNECHT_SHOCKER, "Shocker", 218, "Landsknecht", 16, EO1SkillType.CHASE, EO1Element.THUNDER, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.LEG, EO1SkillMastery.SWORD, EO1SkillTarget.ALL, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[8,8,9,9,10,10,10,10,10,10]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[140,145,150,155,165,167,170,173,176,190]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[200,200,200,200,200,200,200,200,200,200])]),
    EO1SkillData(EO1Skills.LANDSKNECHT_FREEZER, "Freezer", 219, "Landsknecht", 15, EO1SkillType.CHASE, EO1Element.ICE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.LEG, EO1SkillMastery.SWORD, EO1SkillTarget.ALL, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[8,8,9,9,10,10,10,10,10,10]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[140,145,150,155,165,167,170,173,176,190]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[200,200,200,200,200,200,200,200,200,200])]),
    EO1SkillData(EO1Skills.LANDSKNECHT_FLEE, "Flee", 220, "Landsknecht", 10, EO1SkillType.SPECIAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.LEG, EO1SkillMastery.NONE, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,4,4,4,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[60,64,68,72,80,82,84,86,88,98]),EO1SkillValue(EO1SkillValueType.RATE_X1,[50,50,50,50,50,45,40,35,30,25])]),
]

SURVIVALIST_SKILLS: list[EO1SkillData] = [
    EO1SkillData(EO1Skills.SURVIVALIST_HP_UP, "HP Up", 221, "Survivalist", 0, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_HP,[110,112,114,116,128,130,132,134,136,150])]),
    EO1SkillData(EO1Skills.SURVIVALIST_TP_UP, "TP Up", 222, "Survivalist", 1, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_TP,[110,112,114,116,128,130,132,134,136,150])]),
    EO1SkillData(EO1Skills.SURVIVALIST_AGI_UP, "AGI Up", 223, "Survivalist", 2, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_AGI,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.SURVIVALIST_BOWS, "Bows", 224, "Survivalist", 3, EO1SkillType.MASTERY, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.SKILL_MASTER_COEFFICIENT,[110,112,114,116,128,130,132,134,136,150])]),
    EO1SkillData(EO1Skills.SURVIVALIST_1ST_HIT, "1st Hit", 225, "Survivalist", 6, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.RATE_X1,[16,17,18,19,22,23,24,25,26,30])]),
    EO1SkillData(EO1Skills.SURVIVALIST_AMBUSH, "Ambush", 226, "Survivalist", 4, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.VALX1,[16,17,18,19,22,23,24,25,26,30])]),
    EO1SkillData(EO1Skills.SURVIVALIST_CHOP, "Chop", 227, "Survivalist", 18, EO1SkillType.GATHERING, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.GET_SUCCESS_COEFFICIENT,[100,102,104,106,110,111,112,113,114,120])]),
    EO1SkillData(EO1Skills.SURVIVALIST_MINE, "Mine", 228, "Survivalist", 19, EO1SkillType.GATHERING, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.GET_SUCCESS_COEFFICIENT,[100,102,104,106,110,111,112,113,114,120])]),
    EO1SkillData(EO1Skills.SURVIVALIST_TAKE, "Take", 229, "Survivalist", 20, EO1SkillType.GATHERING, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.GET_SUCCESS_COEFFICIENT,[100,102,104,106,110,111,112,113,114,120])]),
    EO1SkillData(EO1Skills.SURVIVALIST_1ST_TURN, "1st Turn", 230, "Survivalist", 11, EO1SkillType.SPECIAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.LEG, EO1SkillMastery.NONE, EO1SkillTarget.ONE, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[10,9,8,7,6,5,4,3,2,1]),EO1SkillValue(EO1SkillValueType.RATE_X1,[70,75,80,85,100,100,100,100,100,100])]),
    EO1SkillData(EO1Skills.SURVIVALIST_TRICKERY, "Trickery", 231, "Survivalist", 7, EO1SkillType.DEBUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.LEG, EO1SkillMastery.NONE, EO1SkillTarget.ALL, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.HIT, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[2,2,2,2,3,3,3,3,3,3]),EO1SkillValue(EO1SkillValueType.SPEED,[80,80,80,80,80,80,80,80,80,80]),EO1SkillValue(EO1SkillValueType.MUL_HIT,[85,83,81,79,75,74,73,72,71,70])]),
    EO1SkillData(EO1Skills.SURVIVALIST_QUICKEN, "Quicken", 232, "Survivalist", 8, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.LEG, EO1SkillMastery.NONE, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.SPEED, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[2,2,2,2,3,3,3,3,3,3]),EO1SkillValue(EO1SkillValueType.SPEED,[80,80,80,80,80,80,80,80,80,80]),EO1SkillValue(EO1SkillValueType.MUL_ACTION_SPEED,[110,115,120,125,130,131,132,133,134,140])]),
    EO1SkillData(EO1Skills.SURVIVALIST_TRUESHOT, "Trueshot", 233, "Survivalist", 12, EO1SkillType.PHYSICAL_ATTACK, EO1Element.STAB, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.ARM, EO1SkillMastery.SHOT, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[140,145,150,155,165,167,170,173,176,190]),EO1SkillValue(EO1SkillValueType.SPEED,[50,50,50,50,50,50,50,50,50,50]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120])]),
    EO1SkillData(EO1Skills.SURVIVALIST_MULTIHIT, "Multihit", 234, "Survivalist", 13, EO1SkillType.PHYSICAL_ATTACK, EO1Element.STAB, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.ARM, EO1SkillMastery.SHOT, EO1SkillTarget.ALL_RAND, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[8,8,9,9,10,10,10,10,10,10]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[100,103,106,109,115,116,117,118,119,125]),EO1SkillValue(EO1SkillValueType.SPEED,[50,50,50,50,50,50,50,50,50,50]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120]),EO1SkillValue(EO1SkillValueType.ATTACK_NUMBER,[2,2,2,2,2,2,2,2,2,3])]),
    EO1SkillData(EO1Skills.SURVIVALIST_DISABLE, "Disable", 235, "Survivalist", 14, EO1SkillType.PHYSICAL_ATTACK, EO1Element.STAB, EO1Element.NONE, EO1Ailment.LEG_BIND, EO1SkillNeed.ARM, EO1SkillMastery.SHOT, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[130,131,132,133,134,135,136,137,138,140]),EO1SkillValue(EO1SkillValueType.SPEED,[50,50,50,50,50,50,50,50,50,50]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[20,21,22,23,29,30,31,32,33,40])]),
    EO1SkillData(EO1Skills.SURVIVALIST_APOLLON, "Apollon", 236, "Survivalist", 15, EO1SkillType.SPECIAL, EO1Element.STAB, EO1Element.NONE, EO1Ailment.STUN, EO1SkillNeed.ARM, EO1SkillMastery.SHOT, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[8,9,10,11,12,12,12,12,12,12]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[300,310,320,330,390,400,410,420,430,500]),EO1SkillValue(EO1SkillValueType.SPEED,[20,20,20,20,20,20,20,20,20,20]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[0,0,0,0,10,15,20,25,30,40]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[200,200,200,200,200,200,200,200,200,200])]),
    EO1SkillData(EO1Skills.SURVIVALIST_CLOAK, "Cloak", 237, "Survivalist", 9, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.LEG, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.AVOID, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[2,2,2,2,3,3,3,3,3,3]),EO1SkillValue(EO1SkillValueType.SPEED,[80,80,80,80,80,80,80,80,80,80]),EO1SkillValue(EO1SkillValueType.MUL_TARGET,[50,45,40,35,25,24,23,22,21,20])]),
    EO1SkillData(EO1Skills.SURVIVALIST_ESCAPE, "Escape", 238, "Survivalist", 10, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.LEG, EO1SkillMastery.NONE, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.STYLE, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.SPEED,[80,80,80,80,80,80,80,80,80,80]),EO1SkillValue(EO1SkillValueType.MUL_DEFENSE,[100,100,100,100,110,111,112,113,114,119]),EO1SkillValue(EO1SkillValueType.ESCAPE_RATE,[120,121,122,123,129,130,131,132,133,140])]),
    EO1SkillData(EO1Skills.SURVIVALIST_AWARE, "Aware", 239, "Survivalist", 5, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.RATE_X1,[16,17,18,19,22,23,24,25,26,30])]),
    EO1SkillData(EO1Skills.SURVIVALIST_STALKER, "Stalker", 240, "Survivalist", 17, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.DUNGEON, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[2,2,3,3,4,4,4,4,4,4]),EO1SkillValue(EO1SkillValueType.TURN_NUMBER,[30,35,40,45,60,65,70,75,80,100]),EO1SkillValue(EO1SkillValueType.RATE_X1,[70,70,70,70,70,65,65,60,60,50])]),
    EO1SkillData(EO1Skills.SURVIVALIST_OWL_EYE, "Owl-Eye", 241, "Survivalist", 16, EO1SkillType.SPECIAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.DUNGEON, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[2,2,3,3,4,4,4,4,4,4]),EO1SkillValue(EO1SkillValueType.TURN_NUMBER,[16,18,20,22,30,32,34,36,38,50]),EO1SkillValue(EO1SkillValueType.VALX1,[2,2,3,3,4,4,5,5,6,6])]),
]

PROTECTOR_SKILLS: list[EO1SkillData] = [
    EO1SkillData(EO1Skills.PROTECTOR_HP_UP, "HP Up", 242, "Protector", 0, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_HP,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.PROTECTOR_TP_UP, "TP Up", 243, "Protector", 1, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_TP,[110,112,114,116,128,130,132,134,136,150])]),
    EO1SkillData(EO1Skills.PROTECTOR_DEF_UP, "DEF Up", 244, "Protector", 2, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_AFFINITY_ALL,[95,94,93,92,91,90,89,88,87,85])]),
    EO1SkillData(EO1Skills.PROTECTOR_SHIELDS, "Shields", 245, "Protector", 3, EO1SkillType.MASTERY, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.SKILL_MASTER_COEFFICIENT,[95,94,93,92,91,90,89,88,87,85])]),
    EO1SkillData(EO1Skills.PROTECTOR_AEGIS, "Aegis", 246, "Protector", 4, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.RATE_X1,[20,21,22,23,29,30,31,32,33,40])]),
    EO1SkillData(EO1Skills.PROTECTOR_EN_GARDE, "En Garde", 247, "Protector", 5, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.RATE_X1,[10,11,12,13,16,17,18,19,20,23])]),
    EO1SkillData(EO1Skills.PROTECTOR_MINE, "Mine", 248, "Protector", 20, EO1SkillType.GATHERING, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.GET_SUCCESS_COEFFICIENT,[100,102,104,106,110,111,112,113,114,120])]),
    EO1SkillData(EO1Skills.PROTECTOR_PROVOKE, "Provoke", 249, "Protector", 6, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.DEFENCE, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[2,2,2,2,3,3,3,3,3,3]),EO1SkillValue(EO1SkillValueType.SPEED,[80,82,84,86,90,92,94,96,98,102]),EO1SkillValue(EO1SkillValueType.MUL_TARGET,[160,170,180,190,200,200,200,200,200,200]),EO1SkillValue(EO1SkillValueType.MUL_AFFINITY,[100,100,100,100,100,90,89,88,87,85])]),
    EO1SkillData(EO1Skills.PROTECTOR_F_GUARD, "F. Guard", 250, "Protector", 11, EO1SkillType.DEFENSE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.ARM, EO1SkillMastery.NONE, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.RATE_X1,[20,23,26,29,35,36,37,38,39,40])]),
    EO1SkillData(EO1Skills.PROTECTOR_B_GUARD, "B. Guard", 251, "Protector", 12, EO1SkillType.DEFENSE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.ARM, EO1SkillMastery.NONE, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.RATE_X1,[20,23,26,29,35,36,37,38,39,40])]),
    EO1SkillData(EO1Skills.PROTECTOR_PARRY, "Parry", 252, "Protector", 8, EO1SkillType.DEFENSE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.ARM, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.COUNTER_RATE,[70,75,80,85,100,100,100,100,100,100]),EO1SkillValue(EO1SkillValueType.COUNTER_DEC_RATE,[100,100,100,100,95,90,85,80,75,65])]),
    EO1SkillData(EO1Skills.PROTECTOR_FORTIFY, "Fortify", 253, "Protector", 9, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.DEFENCE, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.SPEED,[80,82,84,86,90,92,94,96,98,102]),EO1SkillValue(EO1SkillValueType.MUL_AFFINITY,[80,77,74,71,68,67,66,65,65,64])]),
    EO1SkillData(EO1Skills.PROTECTOR_DEFENDER, "Defender", 254, "Protector", 10, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.NONE, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.DEFENCE, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[8,9,10,11,12,12,12,12,12,12]),EO1SkillValue(EO1SkillValueType.SPEED,[80,82,84,86,90,92,94,96,98,102]),EO1SkillValue(EO1SkillValueType.MUL_AFFINITY,[80,77,74,71,68,67,66,65,65,64])]),
    EO1SkillData(EO1Skills.PROTECTOR_SMITE, "Smite", 255, "Protector", 16, EO1SkillType.PHYSICAL_ATTACK, EO1Element.BASH, EO1Element.NONE, EO1Ailment.ARM_BIND, EO1SkillNeed.ARM, EO1SkillMastery.SHIELD, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[10,11,12,13,14,14,14,14,14,14]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[210,215,220,225,235,237,240,243,246,260]),EO1SkillValue(EO1SkillValueType.SPEED,[20,20,20,20,20,20,20,20,20,20]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[200,200,200,200,200,200,200,200,200,200]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[0,0,0,0,10,11,12,13,14,20])]),
    EO1SkillData(EO1Skills.PROTECTOR_ANTIFIRE, "Antifire", 256, "Protector", 13, EO1SkillType.DEFENSE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.ARM, EO1SkillMastery.SHIELD, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[6,6,7,7,8,8,8,8,8,8]),EO1SkillValue(EO1SkillValueType.MUL_AFFINITY,[50,40,30,20,0,100,100,100,100,100]),EO1SkillValue(EO1SkillValueType.ABSORPTION_RATE,[0,0,0,0,0,2,4,6,8,10])]),
    EO1SkillData(EO1Skills.PROTECTOR_ANTIVOLT, "Antivolt", 257, "Protector", 14, EO1SkillType.DEFENSE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.ARM, EO1SkillMastery.SHIELD, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[6,6,7,7,8,8,8,8,8,8]),EO1SkillValue(EO1SkillValueType.MUL_AFFINITY,[50,40,30,20,0,100,100,100,100,100]),EO1SkillValue(EO1SkillValueType.ABSORPTION_RATE,[0,0,0,0,0,2,4,6,8,10])]),
    EO1SkillData(EO1Skills.PROTECTOR_ANTICOLD, "Anticold", 258, "Protector", 15, EO1SkillType.DEFENSE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.ARM, EO1SkillMastery.SHIELD, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[6,6,7,7,8,8,8,8,8,8]),EO1SkillValue(EO1SkillValueType.MUL_AFFINITY,[50,40,30,20,0,100,100,100,100,100]),EO1SkillValue(EO1SkillValueType.ABSORPTION_RATE,[0,0,0,0,0,2,4,6,8,10])]),
    EO1SkillData(EO1Skills.PROTECTOR_CURE, "Cure", 259, "Protector", 17, EO1SkillType.HEAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.NONE, EO1SkillTarget.ONE, EO1SkillSide.SELF, EO1SkillUsage.ALL, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[100,100,100,100,100,100,100,100,100,100]),EO1SkillValue(EO1SkillValueType.SPEED,[70,72,74,76,80,82,84,86,88,92]),EO1SkillValue(EO1SkillValueType.RECOVERY_VALUE,[17,22,27,32,42,47,52,57,62,77])]),
    EO1SkillData(EO1Skills.PROTECTOR_CURE_II, "Cure II", 260, "Protector", 18, EO1SkillType.HEAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.NONE, EO1SkillTarget.ONE, EO1SkillSide.SELF, EO1SkillUsage.ALL, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[10,11,12,13,14,14,14,14,14,14]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[100,100,100,100,100,100,100,100,100,100]),EO1SkillValue(EO1SkillValueType.SPEED,[20,22,24,26,30,32,34,36,38,42]),EO1SkillValue(EO1SkillValueType.RECOVERY_VALUE,[63,68,73,78,93,98,103,108,113,133])]),
    EO1SkillData(EO1Skills.PROTECTOR_FLEE, "Flee", 261, "Protector", 7, EO1SkillType.SPECIAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.LEG, EO1SkillMastery.NONE, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,4,4,4,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[60,64,68,72,80,82,84,86,88,98]),EO1SkillValue(EO1SkillValueType.RATE_X1,[50,50,50,50,50,45,40,35,30,25])]),
    EO1SkillData(EO1Skills.PROTECTOR_STALKER, "Stalker", 262, "Protector", 19, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.DUNGEON, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[2,2,3,3,4,4,4,4,4,4]),EO1SkillValue(EO1SkillValueType.TURN_NUMBER,[30,35,40,45,60,65,70,75,80,100]),EO1SkillValue(EO1SkillValueType.RATE_X1,[70,70,70,70,70,65,65,60,60,50])]),
]

DARK_HUNTER_SKILLS: list[EO1SkillData] = [
    EO1SkillData(EO1Skills.DARK_HUNTER_HP_UP, "HP Up", 263, "Dark Hunter", 0, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_HP,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.DARK_HUNTER_TP_UP, "TP Up", 264, "Dark Hunter", 1, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_TP,[110,112,114,116,128,130,132,134,136,150])]),
    EO1SkillData(EO1Skills.DARK_HUNTER_ATK_UP, "ATK Up", 265, "Dark Hunter", 2, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.ATTACK_BOOST_COEFFICIENT,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.DARK_HUNTER_WHIPS, "Whips", 266, "Dark Hunter", 3, EO1SkillType.MASTERY, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.SKILL_MASTER_COEFFICIENT,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.DARK_HUNTER_SWORDS, "Swords", 267, "Dark Hunter", 4, EO1SkillType.MASTERY, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.SKILL_MASTER_COEFFICIENT,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.DARK_HUNTER_BOOST_UP, "Boost Up", 268, "Dark Hunter", 5, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_BOOSTADD,[1,1,2,2,3,3,4,4,5,5])]),
    EO1SkillData(EO1Skills.DARK_HUNTER_FURY, "Fury", 269, "Dark Hunter", 6, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.RATE_X1,[30,30,30,30,30,34,38,42,46,50]),EO1SkillValue(EO1SkillValueType.VALX1,[10,15,20,25,30,20,20,20,20,20])]),
    EO1SkillData(EO1Skills.DARK_HUNTER_TAKE, "Take", 270, "Dark Hunter", 20, EO1SkillType.GATHERING, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.GET_SUCCESS_COEFFICIENT,[100,102,104,106,110,111,112,113,114,120])]),
    EO1SkillData(EO1Skills.DARK_HUNTER_CLOAK, "Cloak", 271, "Dark Hunter", 7, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.LEG, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.AVOID, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[2,2,2,2,3,3,3,3,3,3]),EO1SkillValue(EO1SkillValueType.SPEED,[110,110,110,110,110,110,110,110,110,110]),EO1SkillValue(EO1SkillValueType.MUL_TARGET,[50,48,46,44,40,38,36,34,32,26])]),
    EO1SkillData(EO1Skills.DARK_HUNTER_VIPER, "Viper", 272, "Dark Hunter", 8, EO1SkillType.PHYSICAL_ATTACK, EO1Element.SLASH, EO1Element.NONE, EO1Ailment.POISON, EO1SkillNeed.ARM, EO1SkillMastery.WHIP, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[130,135,140,145,150,155,160,165,170,180]),EO1SkillValue(EO1SkillValueType.SPEED,[80,80,80,80,80,80,80,80,80,80]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120]),EO1SkillValue(EO1SkillValueType.EFFICACY_SKILL_COEFFICIENT,[4,7,10,13,18,21,24,27,30,37]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[50,51,52,53,59,60,61,62,63,70])]),
    EO1SkillData(EO1Skills.DARK_HUNTER_GAG, "Gag", 273, "Dark Hunter", 9, EO1SkillType.PHYSICAL_ATTACK, EO1Element.SLASH, EO1Element.NONE, EO1Ailment.HEAD_BIND, EO1SkillNeed.ARM, EO1SkillMastery.WHIP, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[130,135,140,145,150,155,160,165,170,180]),EO1SkillValue(EO1SkillValueType.SPEED,[80,80,80,80,80,80,80,80,80,80]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[35,36,41,38,44,45,46,47,48,55])]),
    EO1SkillData(EO1Skills.DARK_HUNTER_CUFFS, "Cuffs", 274, "Dark Hunter", 11, EO1SkillType.PHYSICAL_ATTACK, EO1Element.SLASH, EO1Element.NONE, EO1Ailment.ARM_BIND, EO1SkillNeed.ARM, EO1SkillMastery.WHIP, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[130,135,140,145,150,155,160,165,170,180]),EO1SkillValue(EO1SkillValueType.SPEED,[80,80,80,80,80,80,80,80,80,80]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[35,36,41,38,44,45,46,47,48,55])]),
    EO1SkillData(EO1Skills.DARK_HUNTER_SHACKLES, "Shackles", 275, "Dark Hunter", 10, EO1SkillType.PHYSICAL_ATTACK, EO1Element.SLASH, EO1Element.NONE, EO1Ailment.LEG_BIND, EO1SkillNeed.ARM, EO1SkillMastery.WHIP, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[130,135,140,145,150,155,160,165,170,180]),EO1SkillValue(EO1SkillValueType.SPEED,[80,80,80,80,80,80,80,80,80,80]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[35,36,41,38,44,45,46,47,48,55])]),
    EO1SkillData(EO1Skills.DARK_HUNTER_ECSTASY, "Ecstasy", 276, "Dark Hunter", 12, EO1SkillType.SPECIAL, EO1Element.SLASH, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.ARM, EO1SkillMastery.WHIP, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[8,9,10,11,12,12,12,12,12,12]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[500,510,520,530,590,600,610,620,630,700]),EO1SkillValue(EO1SkillValueType.SPEED,[20,20,20,20,20,20,20,20,20,20]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[200,200,200,200,200,200,200,200,200,200])]),
    EO1SkillData(EO1Skills.DARK_HUNTER_CLIMAX, "Climax", 277, "Dark Hunter", 13, EO1SkillType.SPECIAL, EO1Element.SLASH, EO1Element.NONE, EO1Ailment.INSTANT_DEATH, EO1SkillNeed.ARM, EO1SkillMastery.WHIP, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[6,6,7,7,8,8,8,8,8,8]),EO1SkillValue(EO1SkillValueType.RATE_X1,[5,6,7,8,14,15,16,17,18,25]),EO1SkillValue(EO1SkillValueType.SPEED,[20,20,20,20,20,20,20,20,20,20]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[75,75,75,75,75,75,75,75,75,75])]),
    EO1SkillData(EO1Skills.DARK_HUNTER_HYPNOS, "Hypnos", 278, "Dark Hunter", 14, EO1SkillType.PHYSICAL_ATTACK, EO1Element.STAB, EO1Element.NONE, EO1Ailment.SLEEP, EO1SkillNeed.ARM, EO1SkillMastery.SWORD, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[140,145,150,155,165,167,170,173,176,190]),EO1SkillValue(EO1SkillValueType.SPEED,[80,80,80,80,80,80,80,80,80,80]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[40,41,42,43,49,50,51,52,53,60])]),
    EO1SkillData(EO1Skills.DARK_HUNTER_NERVE, "Nerve", 279, "Dark Hunter", 15, EO1SkillType.PHYSICAL_ATTACK, EO1Element.STAB, EO1Element.NONE, EO1Ailment.PARALYSIS, EO1SkillNeed.ARM, EO1SkillMastery.SWORD, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[140,145,150,155,165,167,170,173,176,190]),EO1SkillValue(EO1SkillValueType.SPEED,[80,80,80,80,80,80,80,80,80,80]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[40,41,42,43,49,50,51,52,53,60])]),
    EO1SkillData(EO1Skills.DARK_HUNTER_PETRIFY, "Petrify", 280, "Dark Hunter", 19, EO1SkillType.PHYSICAL_ATTACK, EO1Element.STAB, EO1Element.NONE, EO1Ailment.PETRIFY, EO1SkillNeed.ARM, EO1SkillMastery.SWORD, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[6,6,7,7,8,8,8,8,8,8]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[140,145,150,155,165,167,170,173,176,190]),EO1SkillValue(EO1SkillValueType.SPEED,[20,20,20,20,20,20,20,20,20,20]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[40,41,42,43,49,50,51,52,53,60])]),
    EO1SkillData(EO1Skills.DARK_HUNTER_BAIT, "Bait", 281, "Dark Hunter", 18, EO1SkillType.COUNTER, EO1Element.SLASH, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.ARM, EO1SkillMastery.SWORD, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[8,9,10,11,12,12,12,12,12,12]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[200,210,220,230,250,260,270,280,290,320]),EO1SkillValue(EO1SkillValueType.SC2,[70,70,70,70,100,110,120,130,140,160]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120]),EO1SkillValue(EO1SkillValueType.COUNTER_RATE,[100,100,100,100,100,100,100,100,100,100])]),
    EO1SkillData(EO1Skills.DARK_HUNTER_DRAIN, "Drain", 282, "Dark Hunter", 17, EO1SkillType.PHYSICAL_ATTACK, EO1Element.STAB, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.ARM, EO1SkillMastery.SWORD, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[140,145,150,155,165,167,170,173,176,190]),EO1SkillValue(EO1SkillValueType.SPEED,[80,80,80,80,80,80,80,80,80,80]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120]),EO1SkillValue(EO1SkillValueType.ABSORPTION_RATE,[50,52,54,56,68,70,72,74,76,100])]),
    EO1SkillData(EO1Skills.DARK_HUNTER_MIRAGE, "Mirage", 283, "Dark Hunter", 16, EO1SkillType.PHYSICAL_ATTACK, EO1Element.STAB, EO1Element.NONE, EO1Ailment.CONFUSION, EO1SkillNeed.ARM, EO1SkillMastery.SWORD, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[140,145,150,155,165,167,170,173,176,190]),EO1SkillValue(EO1SkillValueType.SPEED,[80,80,80,80,80,80,80,80,80,80]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[35,36,41,38,44,45,46,47,48,55])]),
]

RONIN_SKILLS: list[EO1SkillData] = [
    EO1SkillData(EO1Skills.RONIN_HP_UP, "HP Up", 284, "Ronin", 0, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_HP,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.RONIN_TP_UP, "TP Up", 285, "Ronin", 1, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_TP,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.RONIN_ATK_UP, "ATK Up", 286, "Ronin", 2, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.ATTACK_BOOST_COEFFICIENT,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.RONIN_KATANAS, "Katanas", 287, "Ronin", 3, EO1SkillType.MASTERY, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.SKILL_MASTER_COEFFICIENT,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.RONIN_CRIT_UP, "Crit Up", 288, "Ronin", 5, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_CRITICAL,[1,2,3,4,5,6,7,8,9,10])]),
    EO1SkillData(EO1Skills.RONIN_SIGHT, "Sight", 289, "Ronin", 4, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.VALX1,[10,11,12,13,19,20,21,22,23,30])]),
    EO1SkillData(EO1Skills.RONIN_MINE, "Mine", 290, "Ronin", 20, EO1SkillType.GATHERING, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.GET_SUCCESS_COEFFICIENT,[100,102,104,106,110,111,112,113,114,120])]),
    EO1SkillData(EO1Skills.RONIN_IBUKI, "Ibuki", 291, "Ronin", 6, EO1SkillType.HEAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[100,100,100,100,100,100,100,100,100,100]),EO1SkillValue(EO1SkillValueType.SPEED,[70,72,74,76,80,82,86,88,90,96]),EO1SkillValue(EO1SkillValueType.RECOVERY_VALUE,[17,22,27,32,42,47,52,57,62,77])]),
    EO1SkillData(EO1Skills.RONIN_KESAGIRI, "Kesagiri", 292, "Ronin", 7, EO1SkillType.PHYSICAL_ATTACK, EO1Element.SLASH, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.LEG, EO1SkillMastery.SAMURAI_SWORD, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[130,135,140,145,150,155,160,165,170,180]),EO1SkillValue(EO1SkillValueType.SPEED,[50,50,50,50,50,50,50,50,50,50]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120])]),
    EO1SkillData(EO1Skills.RONIN_OVERHEAD, "Overhead", 293, "Ronin", 8, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.STYLE, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[2,2,3,3,4,4,4,4,4,4]),EO1SkillValue(EO1SkillValueType.SPEED,[100,100,100,100,100,100,100,100,100,100]),EO1SkillValue(EO1SkillValueType.MUL_AFFINITY,[95,94,93,92,91,90,89,88,87,85]),EO1SkillValue(EO1SkillValueType.MUL_PHYSICAL_ATTACK,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.RONIN_ZAMBA, "Zamba", 294, "Ronin", 9, EO1SkillType.PHYSICAL_ATTACK, EO1Element.SLASH, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.ARM, EO1SkillMastery.SAMURAI_SWORD, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[140,145,150,155,165,167,170,173,176,190]),EO1SkillValue(EO1SkillValueType.SPEED,[50,50,50,50,50,50,50,50,50,50]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120])]),
    EO1SkillData(EO1Skills.RONIN_MIDAREBA, "Midareba", 295, "Ronin", 10, EO1SkillType.PHYSICAL_ATTACK, EO1Element.SLASH, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.ARM, EO1SkillMastery.SAMURAI_SWORD, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[8,9,10,11,12,12,12,12,12,12]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[100,103,106,109,115,116,117,118,119,125]),EO1SkillValue(EO1SkillValueType.SPEED,[50,50,50,50,50,50,50,50,50,50]),EO1SkillValue(EO1SkillValueType.ATTACK_NUMBER,[2,2,2,2,2,2,2,2,2,3]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120])]),
    EO1SkillData(EO1Skills.RONIN_OROCHI, "Orochi", 296, "Ronin", 11, EO1SkillType.PHYSICAL_ATTACK, EO1Element.SLASH, EO1Element.FIRE, EO1Ailment.NONE, EO1SkillNeed.ARM, EO1SkillMastery.SAMURAI_SWORD, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[6,7,8,9,10,10,10,10,10,10]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[130,131,132,133,134,135,136,137,138,140]),EO1SkillValue(EO1SkillValueType.SPEED,[20,20,20,20,20,20,20,20,20,20]),EO1SkillValue(EO1SkillValueType.ATTR_ADD_ATTACK_SC,[50,55,60,70,75,80,85,90,95,100]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120])]),
    EO1SkillData(EO1Skills.RONIN_SEIGAN, "Seigan", 297, "Ronin", 12, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.STYLE, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[2,2,3,3,4,4,4,4,4,4]),EO1SkillValue(EO1SkillValueType.SPEED,[100,100,100,100,100,100,100,100,100,100]),EO1SkillValue(EO1SkillValueType.MUL_AFFINITY,[85,84,83,82,81,80,79,78,77,75]),EO1SkillValue(EO1SkillValueType.MUL_PHYSICAL_ATTACK,[100,101,102,103,109,110,111,112,123,120])]),
    EO1SkillData(EO1Skills.RONIN_MIKIRI, "Mikiri", 298, "Ronin", 13, EO1SkillType.DEFENSE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.ARM, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[10,9,8,7,6,5,4,3,2,1])]),
    EO1SkillData(EO1Skills.RONIN_KOTEUCHI, "Koteuchi", 299, "Ronin", 14, EO1SkillType.PHYSICAL_ATTACK, EO1Element.STAB, EO1Element.NONE, EO1Ailment.ARM_BIND, EO1SkillNeed.ARM, EO1SkillMastery.SAMURAI_SWORD, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[130,131,132,133,134,135,136,137,138,140]),EO1SkillValue(EO1SkillValueType.SPEED,[50,50,50,50,50,50,50,50,50,50]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[20,21,22,23,29,30,31,32,33,40])]),
    EO1SkillData(EO1Skills.RONIN_RAIZUKI, "Raizuki", 300, "Ronin", 15, EO1SkillType.PHYSICAL_ATTACK, EO1Element.STAB, EO1Element.THUNDER, EO1Ailment.NONE, EO1SkillNeed.ARM, EO1SkillMastery.SAMURAI_SWORD, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[6,7,8,9,10,10,10,10,10,10]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[130,131,132,133,134,135,136,137,138,140]),EO1SkillValue(EO1SkillValueType.SPEED,[20,20,20,20,20,20,20,20,20,20]),EO1SkillValue(EO1SkillValueType.ATTR_ADD_ATTACK_SC,[50,55,60,70,75,80,85,90,95,100]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120])]),
    EO1SkillData(EO1Skills.RONIN_IAI, "Iai", 301, "Ronin", 16, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.STYLE, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[2,2,3,3,4,4,4,4,4,4]),EO1SkillValue(EO1SkillValueType.SPEED,[100,100,100,100,100,100,100,100,100,100]),EO1SkillValue(EO1SkillValueType.MUL_ACTION_SPEED,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.RONIN_KUBIUCHI, "Kubiuchi", 302, "Ronin", 17, EO1SkillType.SPECIAL, EO1Element.SLASH, EO1Element.NONE, EO1Ailment.INSTANT_DEATH, EO1SkillNeed.ARM, EO1SkillMastery.SAMURAI_SWORD, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[6,7,8,9,10,10,10,10,10,10]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[130,131,132,133,134,135,136,137,138,140]),EO1SkillValue(EO1SkillValueType.SPEED,[100,100,100,100,100,100,100,100,100,100]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[40,41,42,43,49,50,51,52,53,60])]),
    EO1SkillData(EO1Skills.RONIN_GATOTSU, "Gatotsu", 303, "Ronin", 18, EO1SkillType.PHYSICAL_ATTACK, EO1Element.SLASH, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.ARM, EO1SkillMastery.SAMURAI_SWORD, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[170,171,172,173,189,190,191,192,193,210]),EO1SkillValue(EO1SkillValueType.SPEED,[100,100,100,100,100,100,100,100,100,100]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120])]),
    EO1SkillData(EO1Skills.RONIN_HYOSETSU, "Hyosetsu", 304, "Ronin", 19, EO1SkillType.PHYSICAL_ATTACK, EO1Element.SLASH, EO1Element.ICE, EO1Ailment.NONE, EO1SkillNeed.ARM, EO1SkillMastery.SAMURAI_SWORD, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[6,7,8,9,10,10,10,10,10,10]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[130,131,132,133,134,135,136,137,138,140]),EO1SkillValue(EO1SkillValueType.SPEED,[100,100,100,100,100,100,100,100,100,100]),EO1SkillValue(EO1SkillValueType.ATTR_ADD_ATTACK_SC,[50,55,60,70,75,80,85,90,95,100]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120])]),
]

MEDIC_SKILLS: list[EO1SkillData] = [
    EO1SkillData(EO1Skills.MEDIC_HP_UP, "HP Up", 305, "Medic", 0, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_HP,[110,112,114,116,128,130,132,134,136,150])]),
    EO1SkillData(EO1Skills.MEDIC_TP_UP, "TP Up", 306, "Medic", 1, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_TP,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.MEDIC_ATK_UP, "ATK Up", 307, "Medic", 2, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.ATTACK_BOOST_COEFFICIENT,[110,125,130,145,190,205,220,235,250,300])]),
    EO1SkillData(EO1Skills.MEDIC_HEALER, "Healer", 308, "Medic", 3, EO1SkillType.MASTERY, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.SKILL_MASTER_COEFFICIENT,[110,140,170,200,300,330,360,390,420,550])]),
    EO1SkillData(EO1Skills.MEDIC_PATCH_UP, "Patch Up", 309, "Medic", 4, EO1SkillType.SPECIAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.RATE_X1,[1,2,3,4,6,7,8,9,10,12])]),
    EO1SkillData(EO1Skills.MEDIC_SCAVENGE, "Scavenge", 310, "Medic", 5, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.RATE_X1,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.MEDIC_TP_REGEN, "TP Regen", 311, "Medic", 6, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.VALX1,[1,1,2,2,3,3,4,4,4,5])]),
    EO1SkillData(EO1Skills.MEDIC_CHOP, "Chop", 312, "Medic", 20, EO1SkillType.GATHERING, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.GET_SUCCESS_COEFFICIENT,[100,102,104,106,110,111,112,113,114,120])]),
    EO1SkillData(EO1Skills.MEDIC_CURE, "Cure", 313, "Medic", 7, EO1SkillType.HEAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.RECOVERY, EO1SkillTarget.ONE, EO1SkillSide.SELF, EO1SkillUsage.ALL, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[100,100,100,100,100,100,100,100,100,100]),EO1SkillValue(EO1SkillValueType.SPEED,[70,72,74,76,80,82,84,86,88,92]),EO1SkillValue(EO1SkillValueType.RECOVERY_VALUE,[15,20,25,30,40,45,50,55,60,75])]),
    EO1SkillData(EO1Skills.MEDIC_CURE_II, "Cure II", 314, "Medic", 8, EO1SkillType.HEAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.RECOVERY, EO1SkillTarget.ONE, EO1SkillSide.SELF, EO1SkillUsage.ALL, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[10,11,12,13,14,14,14,14,14,14]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[100,100,100,100,100,100,100,100,100,100]),EO1SkillValue(EO1SkillValueType.SPEED,[20,22,24,26,30,32,34,36,38,42]),EO1SkillValue(EO1SkillValueType.RECOVERY_VALUE,[60,65,70,75,90,95,100,105,110,130])]),
    EO1SkillData(EO1Skills.MEDIC_CURE_III, "Cure III", 315, "Medic", 9, EO1SkillType.HEAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.RECOVERY, EO1SkillTarget.ONE, EO1SkillSide.SELF, EO1SkillUsage.ALL, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[20,19,18,17,15,14,13,12,11,10]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[100,100,100,100,100,100,100,100,100,100]),EO1SkillValue(EO1SkillValueType.SPEED,[5,8,11,14,20,23,26,29,32,40]),EO1SkillValue(EO1SkillValueType.RECOVERY_VALUE,[500,500,500,500,500,500,500,500,500,500])]),
    EO1SkillData(EO1Skills.MEDIC_SALVE, "Salve", 316, "Medic", 10, EO1SkillType.HEAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.RECOVERY, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.ALL, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[6,7,8,9,10,10,10,10,10,10]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[100,100,100,100,100,100,100,100,100,100]),EO1SkillValue(EO1SkillValueType.SPEED,[70,72,74,76,80,82,84,86,88,92]),EO1SkillValue(EO1SkillValueType.RECOVERY_VALUE,[20,25,30,35,45,50,55,60,75,80])]),
    EO1SkillData(EO1Skills.MEDIC_SALVE_II, "Salve II", 317, "Medic", 11, EO1SkillType.HEAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.RECOVERY, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.ALL, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[16,17,18,19,20,20,20,20,20,20]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[100,100,100,100,100,100,100,100,100,100]),EO1SkillValue(EO1SkillValueType.SPEED,[20,22,24,26,30,32,34,36,38,42]),EO1SkillValue(EO1SkillValueType.RECOVERY_VALUE,[75,82,89,96,120,127,134,141,148,180])]),
    EO1SkillData(EO1Skills.MEDIC_REVIVE, "Revive", 318, "Medic", 12, EO1SkillType.HEAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.NONE, EO1SkillTarget.ONE, EO1SkillSide.SELF, EO1SkillUsage.ALL, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[10,11,12,13,14,14,14,14,14,14]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[100,100,100,100,100,100,100,100,100,100]),EO1SkillValue(EO1SkillValueType.SPEED,[20,22,24,26,30,32,34,36,38,42]),EO1SkillValue(EO1SkillValueType.RECOVERY_VALUE,[15,20,25,30,40,45,50,55,60,75])]),
    EO1SkillData(EO1Skills.MEDIC_UNBIND, "Unbind", 319, "Medic", 13, EO1SkillType.AILMENT_HEAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.NONE, EO1SkillTarget.ONE, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,3,3,4,4,4,4,4,4]),EO1SkillValue(EO1SkillValueType.SPEED,[50,52,54,56,60,62,64,66,68,72]),EO1SkillValue(EO1SkillValueType.RECOVERY_VALUE,[1,1,2,2,3,3,3,3,3,3])]),
    EO1SkillData(EO1Skills.MEDIC_REFRESH, "Refresh", 320, "Medic", 14, EO1SkillType.AILMENT_HEAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.NONE, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.ALL, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,3,3,4,4,4,4,4,4]),EO1SkillValue(EO1SkillValueType.SPEED,[50,52,54,56,60,62,64,66,68,72]),EO1SkillValue(EO1SkillValueType.BST_RECOVERY_LEVEL,[1,2,3,4,5,6,7,8,8,8])]),
    EO1SkillData(EO1Skills.MEDIC_IMMUNIZE, "Immunize", 321, "Medic", 15, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.NONE, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.DEFENCE, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[10,11,12,13,14,14,14,14,14,14]),EO1SkillValue(EO1SkillValueType.SPEED,[50,52,54,56,60,62,64,66,68,72]),EO1SkillValue(EO1SkillValueType.MUL_AFFINITY,[85,80,75,70,65,60,55,50,45,40])]),
    EO1SkillData(EO1Skills.MEDIC_CADUCEUS, "Caduceus", 322, "Medic", 18, EO1SkillType.PHYSICAL_ATTACK, EO1Element.BASH, EO1Element.NONE, EO1Ailment.STUN, EO1SkillNeed.ARM, EO1SkillMastery.NONE, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[8,9,10,11,12,12,12,12,12,12]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[200,210,220,230,250,260,270,280,290,320]),EO1SkillValue(EO1SkillValueType.SPEED,[20,20,20,20,20,20,20,20,20,20]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[120,120,120,120,120,120,120,120,120,120]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[15,20,25,30,40,45,50,55,60,75])]),
    EO1SkillData(EO1Skills.MEDIC_CPR, "CPR", 323, "Medic", 16, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.NONE, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.DEFENCE, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[16,17,18,19,20,20,20,20,20,20]),EO1SkillValue(EO1SkillValueType.RATE_X1,[30,31,32,33,39,40,41,42,43,50]),EO1SkillValue(EO1SkillValueType.SPEED,[50,52,54,56,60,62,64,66,68,72])]),
    EO1SkillData(EO1Skills.MEDIC_REGEN, "Regen", 324, "Medic", 17, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.NONE, EO1SkillTarget.ONE, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.RECOVER, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.SPEED,[50,50,50,50,50,50,50,50,50,50]),EO1SkillValue(EO1SkillValueType.HP_RECOVERY_RATE,[5,6,7,8,10,11,12,13,14,16])]),
    EO1SkillData(EO1Skills.MEDIC_H_TOUCH, "H. Touch", 325, "Medic", 19, EO1SkillType.SPECIAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.TOWN_DUNGEON, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.RATE_X1,[25,27,29,31,35,36,37,38,39,40])]),
]

ALCHEMIST_SKILLS: list[EO1SkillData] = [
    EO1SkillData(EO1Skills.ALCHEMIST_TP_UP, "TP Up", 326, "Alchemist", 0, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_TP,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.ALCHEMIST_FIRE_UP, "Fire Up", 327, "Alchemist", 1, EO1SkillType.MASTERY, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.SKILL_MASTER_COEFFICIENT,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.ALCHEMIST_ICE_UP, "Ice Up", 328, "Alchemist", 2, EO1SkillType.MASTERY, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.SKILL_MASTER_COEFFICIENT,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.ALCHEMIST_VOLT_UP, "Volt Up", 329, "Alchemist", 3, EO1SkillType.MASTERY, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.SKILL_MASTER_COEFFICIENT,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.ALCHEMIST_TOXINS, "Toxins", 330, "Alchemist", 4, EO1SkillType.MASTERY, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.SKILL_MASTER_COEFFICIENT,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.ALCHEMIST_SCAVENGE, "Scavenge", 331, "Alchemist", 5, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.RATE_X1,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.ALCHEMIST_TP_REGEN, "TP Regen", 332, "Alchemist", 6, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.VALX1,[1,1,2,2,3,3,4,4,4,5])]),
    EO1SkillData(EO1Skills.ALCHEMIST_CHOP, "Chop", 333, "Alchemist", 20, EO1SkillType.GATHERING, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.GET_SUCCESS_COEFFICIENT,[100,102,104,106,110,111,112,113,114,120])]),
    EO1SkillData(EO1Skills.ALCHEMIST_FIRE, "Fire", 334, "Alchemist", 7, EO1SkillType.MAGICAL_ATTACK, EO1Element.FIRE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.FIRE, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.ATTR_ATTACK_VALUE,[10,10,10,10,10,10,10,10,10,10]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[80,85,90,100,105,110,115,120,125,130]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[200,200,200,200,200,200,200,200,200,200]),EO1SkillValue(EO1SkillValueType.SPEED,[60,60,60,60,60,60,60,60,60,60])]),
    EO1SkillData(EO1Skills.ALCHEMIST_FLAME, "Flame", 335, "Alchemist", 8, EO1SkillType.MAGICAL_ATTACK, EO1Element.FIRE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.FIRE, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[10,11,12,13,14,14,14,14,14,14]),EO1SkillValue(EO1SkillValueType.ATTR_ATTACK_VALUE,[10,10,9,9,8,8,7,7,6,6]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[140,160,180,200,230,250,270,290,310,350]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[200,200,200,200,200,200,200,200,200,200]),EO1SkillValue(EO1SkillValueType.SPEED,[40,40,40,40,40,40,40,40,40,40])]),
    EO1SkillData(EO1Skills.ALCHEMIST_INFERNO, "Inferno", 336, "Alchemist", 9, EO1SkillType.MAGICAL_ATTACK, EO1Element.FIRE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.FIRE, EO1SkillTarget.ALL, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[16,17,18,19,20,20,20,20,20,20]),EO1SkillValue(EO1SkillValueType.ATTR_ATTACK_VALUE,[10,10,9,9,8,8,7,7,6,6]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[112,128,144,160,184,200,216,232,248,280]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[200,200,200,200,200,200,200,200,200,200]),EO1SkillValue(EO1SkillValueType.SPEED,[20,20,20,20,20,20,20,20,20,20])]),
    EO1SkillData(EO1Skills.ALCHEMIST_ICE, "Ice", 337, "Alchemist", 10, EO1SkillType.MAGICAL_ATTACK, EO1Element.ICE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.ICE, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.ATTR_ATTACK_VALUE,[10,10,10,10,10,10,10,10,10,10]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[80,85,90,100,105,110,115,120,125,130]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[200,200,200,200,200,200,200,200,200,200]),EO1SkillValue(EO1SkillValueType.SPEED,[60,60,60,60,60,60,60,60,60,60])]),
    EO1SkillData(EO1Skills.ALCHEMIST_FREEZE, "Freeze", 338, "Alchemist", 11, EO1SkillType.MAGICAL_ATTACK, EO1Element.ICE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.ICE, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[10,11,12,13,14,14,14,14,14,14]),EO1SkillValue(EO1SkillValueType.ATTR_ATTACK_VALUE,[10,10,9,9,8,8,7,7,6,6]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[140,160,180,200,230,250,270,290,310,350]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[200,200,200,200,200,200,200,200,200,200]),EO1SkillValue(EO1SkillValueType.SPEED,[40,40,40,40,40,40,40,40,40,40])]),
    EO1SkillData(EO1Skills.ALCHEMIST_COCYTUS, "Cocytus", 339, "Alchemist", 12, EO1SkillType.MAGICAL_ATTACK, EO1Element.ICE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.ICE, EO1SkillTarget.ALL, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[16,17,18,19,20,20,20,20,20,20]),EO1SkillValue(EO1SkillValueType.ATTR_ATTACK_VALUE,[10,10,9,9,8,8,7,7,6,6]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[112,128,144,160,184,200,216,232,248,280]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[200,200,200,200,200,200,200,200,200,200]),EO1SkillValue(EO1SkillValueType.SPEED,[20,20,20,20,20,20,20,20,20,20])]),
    EO1SkillData(EO1Skills.ALCHEMIST_VOLT, "Volt", 340, "Alchemist", 13, EO1SkillType.MAGICAL_ATTACK, EO1Element.THUNDER, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.THUNDER, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.ATTR_ATTACK_VALUE,[10,10,10,10,10,10,10,10,10,10]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[80,85,90,100,105,110,115,120,125,130]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[200,200,200,200,200,200,200,200,200,200]),EO1SkillValue(EO1SkillValueType.SPEED,[60,60,60,60,60,60,60,60,60,60])]),
    EO1SkillData(EO1Skills.ALCHEMIST_THUNDER, "Thunder", 341, "Alchemist", 14, EO1SkillType.MAGICAL_ATTACK, EO1Element.THUNDER, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.THUNDER, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[10,11,12,13,14,14,14,14,14,14]),EO1SkillValue(EO1SkillValueType.ATTR_ATTACK_VALUE,[10,10,9,9,8,8,7,7,6,6]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[140,160,180,200,230,250,270,290,310,350]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[200,200,200,200,200,200,200,200,200,200]),EO1SkillValue(EO1SkillValueType.SPEED,[40,40,40,40,40,40,40,40,40,40])]),
    EO1SkillData(EO1Skills.ALCHEMIST_THOR, "Thor", 342, "Alchemist", 15, EO1SkillType.MAGICAL_ATTACK, EO1Element.THUNDER, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.THUNDER, EO1SkillTarget.ALL, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[16,17,18,19,20,20,20,20,20,20]),EO1SkillValue(EO1SkillValueType.ATTR_ATTACK_VALUE,[10,10,9,9,8,8,7,7,6,6]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[112,128,144,160,184,200,216,232,248,280]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[200,200,200,200,200,200,200,200,200,200]),EO1SkillValue(EO1SkillValueType.SPEED,[20,20,20,20,20,20,20,20,20,20])]),
    EO1SkillData(EO1Skills.ALCHEMIST_POISON, "Poison", 343, "Alchemist", 16, EO1SkillType.AILMENT_ATTACK, EO1Element.NONE, EO1Element.NONE, EO1Ailment.POISON, EO1SkillNeed.HEAD, EO1SkillMastery.BENOM, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[200,202,204,206,220,222,224,226,228,250]),EO1SkillValue(EO1SkillValueType.EFFICACY_SKILL_COEFFICIENT,[10,20,30,40,60,80,100,120,140,160]),EO1SkillValue(EO1SkillValueType.SPEED,[60,60,60,60,60,60,60,60,60,60])]),
    EO1SkillData(EO1Skills.ALCHEMIST_VENOM, "Venom", 344, "Alchemist", 17, EO1SkillType.AILMENT_ATTACK, EO1Element.NONE, EO1Element.NONE, EO1Ailment.POISON, EO1SkillNeed.HEAD, EO1SkillMastery.BENOM, EO1SkillTarget.ALL, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[10,11,12,13,14,14,14,14,14,14]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[200,202,204,206,220,222,224,226,228,250]),EO1SkillValue(EO1SkillValueType.EFFICACY_SKILL_COEFFICIENT,[10,20,30,40,60,80,100,120,140,160]),EO1SkillValue(EO1SkillValueType.SPEED,[20,20,20,20,20,20,20,20,20,20])]),
    EO1SkillData(EO1Skills.ALCHEMIST_SIGHT, "Sight", 345, "Alchemist", 18, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.DUNGEON, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[10,9,8,7,6,5,4,3,2,1])]),
    EO1SkillData(EO1Skills.ALCHEMIST_WARP, "Warp", 346, "Alchemist", 19, EO1SkillType.SPECIAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.DUNGEON, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[15,14,13,12,10,9,8,7,6,5])]),
]

TROUBADOUR_SKILLS: list[EO1SkillData] = [
    EO1SkillData(EO1Skills.TROUBADOUR_HP_UP, "HP Up", 347, "Troubadour", 0, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_HP,[110,112,114,116,128,130,132,134,136,150])]),
    EO1SkillData(EO1Skills.TROUBADOUR_TP_UP, "TP Up", 348, "Troubadour", 1, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_TP,[110,112,114,116,128,130,132,134,136,150])]),
    EO1SkillData(EO1Skills.TROUBADOUR_SONGS, "Songs", 349, "Troubadour", 2, EO1SkillType.MASTERY, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.SKILL_MASTER_COEFFICIENT,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.TROUBADOUR_DIVINITY, "Divinity", 350, "Troubadour", 3, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_EXP,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.TROUBADOUR_BRAVERY, "Bravery", 351, "Troubadour", 4, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.SONG, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.SPEED,[80,82,84,86,90,92,94,96,98,102]),EO1SkillValue(EO1SkillValueType.MUL_PHYSICAL_ATTACK,[110,115,120,125,130,131,132,133,134,140])]),
    EO1SkillData(EO1Skills.TROUBADOUR_SHELTER, "Shelter", 352, "Troubadour", 5, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.SONG, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.DEFENCE, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.SPEED,[80,82,84,86,90,92,94,96,98,102]),EO1SkillValue(EO1SkillValueType.MUL_DEFENSE,[110,115,120,125,130,131,132,133,134,140])]),
    EO1SkillData(EO1Skills.TROUBADOUR_MERCURY, "Mercury", 353, "Troubadour", 6, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.SONG, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.SPEED, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.SPEED,[80,82,84,86,90,92,94,96,98,102]),EO1SkillValue(EO1SkillValueType.MUL_ACTION_SPEED,[110,115,120,125,130,131,132,133,134,140])]),
    EO1SkillData(EO1Skills.TROUBADOUR_BLAZE, "Blaze", 354, "Troubadour", 10, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.SONG, EO1SkillTarget.ONE, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.AFFINITY, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[15,14,13,12,10,9,8,7,6,5]),EO1SkillValue(EO1SkillValueType.SPEED,[50,52,54,56,60,62,64,66,68,72]),EO1SkillValue(EO1SkillValueType.CHANGE_ATC_ATTR,[0,0,0,0,0,0,0,0,0,0])]),
    EO1SkillData(EO1Skills.TROUBADOUR_FROST, "Frost", 355, "Troubadour", 11, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.SONG, EO1SkillTarget.ONE, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.AFFINITY, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[15,14,13,12,10,9,8,7,6,5]),EO1SkillValue(EO1SkillValueType.SPEED,[50,52,54,56,60,62,64,66,68,72]),EO1SkillValue(EO1SkillValueType.CHANGE_ATC_ATTR,[0,0,0,0,0,0,0,0,0,0])]),
    EO1SkillData(EO1Skills.TROUBADOUR_SHOCK, "Shock", 356, "Troubadour", 12, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.SONG, EO1SkillTarget.ONE, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.AFFINITY, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[15,14,13,12,10,9,8,7,6,5]),EO1SkillValue(EO1SkillValueType.SPEED,[50,52,54,56,60,62,64,66,68,72]),EO1SkillValue(EO1SkillValueType.CHANGE_ATC_ATTR,[0,0,0,0,0,0,0,0,0,0])]),
    EO1SkillData(EO1Skills.TROUBADOUR_ERASURE, "Erasure", 357, "Troubadour", 7, EO1SkillType.BUFF_REMOVAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.SONG, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.SPEED,[80,82,84,86,90,92,94,96,98,102]),EO1SkillValue(EO1SkillValueType.VALX1,[1,1,2,2,3,3,3,3,3,3])]),
    EO1SkillData(EO1Skills.TROUBADOUR_STAMINA, "Stamina", 358, "Troubadour", 9, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.SONG, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.HPMAX, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.SPEED,[50,52,54,56,60,62,64,66,68,72]),EO1SkillValue(EO1SkillValueType.MUL_HP_MAX,[120,123,126,129,135,137,139,141,143,150])]),
    EO1SkillData(EO1Skills.TROUBADOUR_IFRIT, "Ifrit", 359, "Troubadour", 13, EO1SkillType.SPECIAL, EO1Element.FIRE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.SONG, EO1SkillTarget.ALL, EO1SkillSide.ALL, EO1SkillUsage.BATTLE, EO1SkillEffect.AFFINITY, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[6,6,7,7,8,8,8,8,8,8]),EO1SkillValue(EO1SkillValueType.SPEED,[50,52,54,56,60,62,64,66,68,72]),EO1SkillValue(EO1SkillValueType.MUL_AFFINITY,[80,75,70,65,60,55,50,45,40,35]),EO1SkillValue(EO1SkillValueType.MUL_AFFINITY2,[110,115,120,125,130,131,132,133,134,140])]),
    EO1SkillData(EO1Skills.TROUBADOUR_YMIR, "Ymir", 360, "Troubadour", 14, EO1SkillType.SPECIAL, EO1Element.ICE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.SONG, EO1SkillTarget.ALL, EO1SkillSide.ALL, EO1SkillUsage.BATTLE, EO1SkillEffect.AFFINITY, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[6,6,7,7,8,8,8,8,8,8]),EO1SkillValue(EO1SkillValueType.SPEED,[50,52,54,56,60,62,64,66,68,72]),EO1SkillValue(EO1SkillValueType.MUL_AFFINITY,[80,75,70,65,60,55,50,45,40,35]),EO1SkillValue(EO1SkillValueType.MUL_AFFINITY2,[110,115,120,125,130,131,132,133,134,140])]),
    EO1SkillData(EO1Skills.TROUBADOUR_TARANIS, "Taranis", 361, "Troubadour", 15, EO1SkillType.SPECIAL, EO1Element.THUNDER, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.SONG, EO1SkillTarget.ALL, EO1SkillSide.ALL, EO1SkillUsage.BATTLE, EO1SkillEffect.AFFINITY, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[6,6,7,7,8,8,8,8,8,8]),EO1SkillValue(EO1SkillValueType.SPEED,[50,52,54,56,60,62,64,66,68,72]),EO1SkillValue(EO1SkillValueType.MUL_AFFINITY,[80,75,70,65,60,55,50,45,40,35]),EO1SkillValue(EO1SkillValueType.MUL_AFFINITY2,[110,115,120,125,130,131,132,133,134,140])]),
    EO1SkillData(EO1Skills.TROUBADOUR_HEALING, "Healing", 362, "Troubadour", 16, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.SONG, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.RECOVER, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.SPEED,[50,52,54,56,60,62,64,66,68,72]),EO1SkillValue(EO1SkillValueType.HP_RECOVERY_RATE,[2,3,4,5,7,8,9,10,11,13])]),
    EO1SkillData(EO1Skills.TROUBADOUR_RELAXING, "Relaxing", 363, "Troubadour", 17, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.SONG, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.RECOVER, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.SPEED,[50,52,54,56,60,62,64,66,68,72]),EO1SkillValue(EO1SkillValueType.TP_RECOVERY_RATE,[1,1,2,2,3,3,4,4,4,5])]),
    EO1SkillData(EO1Skills.TROUBADOUR_RECOVERY, "Recovery", 364, "Troubadour", 8, EO1SkillType.BUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.SONG, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.BATTLE, EO1SkillEffect.RECOVER, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.SPEED,[50,52,54,56,60,62,64,66,68,72]),EO1SkillValue(EO1SkillValueType.BST_RECOVERY_TURN_CORRECTION,[110,130,150,170,200,220,240,260,280,320])]),
    EO1SkillData(EO1Skills.TROUBADOUR_STALKER, "Stalker", 365, "Troubadour", 18, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.DUNGEON, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[2,2,3,3,4,4,4,4,4,4]),EO1SkillValue(EO1SkillValueType.TURN_NUMBER,[30,35,40,45,60,65,70,75,80,100]),EO1SkillValue(EO1SkillValueType.RATE_X1,[70,70,70,70,70,65,65,60,60,50])]),
    EO1SkillData(EO1Skills.TROUBADOUR_RETURN, "Return", 366, "Troubadour", 19, EO1SkillType.SPECIAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.DUNGEON, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[10,9,8,7,6,5,4,3,2,1])]),
    EO1SkillData(EO1Skills.TROUBADOUR_TAKE, "Take", 367, "Troubadour", 20, EO1SkillType.GATHERING, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.GET_SUCCESS_COEFFICIENT,[100,102,104,106,110,111,112,113,114,120])]),
]

HEXER_SKILLS: list[EO1SkillData] = [
    EO1SkillData(EO1Skills.HEXER_HP_UP, "HP Up", 368, "Hexer", 0, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_HP,[110,112,114,116,128,130,132,134,136,150])]),
    EO1SkillData(EO1Skills.HEXER_TP_UP, "TP Up", 369, "Hexer", 1, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.PARAM_BOOST_TP,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.HEXER_CURSES, "Curses", 370, "Hexer", 2, EO1SkillType.MASTERY, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.SKILL_MASTER_COEFFICIENT,[110,111,112,113,119,120,121,122,123,130])]),
    EO1SkillData(EO1Skills.HEXER_STAGGER, "Stagger", 371, "Hexer", 3, EO1SkillType.SPECIAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.SELF, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.RATE_X1,[16,17,18,19,22,23,24,25,26,30])]),
    EO1SkillData(EO1Skills.HEXER_MINE, "Mine", 372, "Hexer", 20, EO1SkillType.GATHERING, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.SELF, EO1SkillSide.OTHER, EO1SkillUsage.NONE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.GET_SUCCESS_COEFFICIENT,[100,102,104,106,110,111,112,113,114,120])]),
    EO1SkillData(EO1Skills.HEXER_SAPPING, "Sapping", 373, "Hexer", 4, EO1SkillType.DEBUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.CURSE, EO1SkillTarget.ALL, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.SPEED,[50,50,50,50,50,50,50,50,50,50]),EO1SkillValue(EO1SkillValueType.MUL_PHYSICAL_ATTACK,[80,77,74,71,68,67,66,65,64,60])]),
    EO1SkillData(EO1Skills.HEXER_FRAILTY, "Frailty", 374, "Hexer", 5, EO1SkillType.DEBUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.CURSE, EO1SkillTarget.ALL, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.DEFENCE, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.SPEED,[50,50,50,50,50,50,50,50,50,50]),EO1SkillValue(EO1SkillValueType.MUL_DEFENSE,[80,77,74,71,68,67,66,65,64,60])]),
    EO1SkillData(EO1Skills.HEXER_LEADEN, "Leaden", 375, "Hexer", 6, EO1SkillType.DEBUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.CURSE, EO1SkillTarget.ALL, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.SPEED, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.SPEED,[50,50,50,50,50,50,50,50,50,50]),EO1SkillValue(EO1SkillValueType.MUL_ACTION_SPEED,[80,77,74,71,68,67,66,65,64,60])]),
    EO1SkillData(EO1Skills.HEXER_RELAPSE, "Relapse", 376, "Hexer", 8, EO1SkillType.DEBUFF, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.CURSE, EO1SkillTarget.ALL, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.RECOVER, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[4,4,5,5,6,6,6,6,6,6]),EO1SkillValue(EO1SkillValueType.SPEED,[50,50,50,50,50,50,50,50,50,50]),EO1SkillValue(EO1SkillValueType.BST_RECOVERY_TURN_CORRECTION,[90,87,84,81,72,68,65,62,59,50])]),
    EO1SkillData(EO1Skills.HEXER_CRANIAL, "Cranial", 377, "Hexer", 9, EO1SkillType.AILMENT_ATTACK, EO1Element.NONE, EO1Element.NONE, EO1Ailment.HEAD_BIND, EO1SkillNeed.HEAD, EO1SkillMastery.CURSE, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[50,51,52,53,59,60,61,62,63,70]),EO1SkillValue(EO1SkillValueType.SPEED,[100,100,100,100,100,100,100,100,100,100])]),
    EO1SkillData(EO1Skills.HEXER_ABDOMEN, "Abdomen", 378, "Hexer", 10, EO1SkillType.AILMENT_ATTACK, EO1Element.NONE, EO1Element.NONE, EO1Ailment.ARM_BIND, EO1SkillNeed.HEAD, EO1SkillMastery.CURSE, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[50,51,52,53,59,60,61,62,63,70]),EO1SkillValue(EO1SkillValueType.SPEED,[100,100,100,100,100,100,100,100,100,100])]),
    EO1SkillData(EO1Skills.HEXER_IMMOBILE, "Immobile", 379, "Hexer", 11, EO1SkillType.AILMENT_ATTACK, EO1Element.NONE, EO1Element.NONE, EO1Ailment.LEG_BIND, EO1SkillNeed.HEAD, EO1SkillMastery.CURSE, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[3,3,4,4,5,5,5,5,5,5]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[50,51,52,53,59,60,61,62,63,70]),EO1SkillValue(EO1SkillValueType.SPEED,[100,100,100,100,100,100,100,100,100,100])]),
    EO1SkillData(EO1Skills.HEXER_BLINDING, "Blinding", 380, "Hexer", 7, EO1SkillType.AILMENT_ATTACK, EO1Element.NONE, EO1Element.NONE, EO1Ailment.BLIND, EO1SkillNeed.HEAD, EO1SkillMastery.CURSE, EO1SkillTarget.ALL, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[6,7,8,9,10,10,10,10,10,10]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[50,51,52,53,59,60,61,62,63,70]),EO1SkillValue(EO1SkillValueType.SPEED,[50,50,50,50,50,50,50,50,50,50])]),
    EO1SkillData(EO1Skills.HEXER_TORPOR, "Torpor", 381, "Hexer", 12, EO1SkillType.AILMENT_ATTACK, EO1Element.NONE, EO1Element.NONE, EO1Ailment.SLEEP, EO1SkillNeed.HEAD, EO1SkillMastery.CURSE, EO1SkillTarget.ALL, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[6,7,8,9,10,10,10,10,10,10]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[50,51,52,53,59,60,61,62,63,70]),EO1SkillValue(EO1SkillValueType.SPEED,[50,50,50,50,50,50,50,50,50,50])]),
    EO1SkillData(EO1Skills.HEXER_CORRUPT, "Corrupt", 382, "Hexer", 13, EO1SkillType.AILMENT_ATTACK, EO1Element.NONE, EO1Element.NONE, EO1Ailment.CURSE, EO1SkillNeed.HEAD, EO1SkillMastery.CURSE, EO1SkillTarget.ALL, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[6,7,8,9,10,10,10,10,10,10]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[50,51,52,53,59,60,61,62,63,70]),EO1SkillValue(EO1SkillValueType.SPEED,[50,50,50,50,50,50,50,50,50,50])]),
    EO1SkillData(EO1Skills.HEXER_EVIL_EYE, "Evil Eye", 383, "Hexer", 15, EO1SkillType.AILMENT_ATTACK, EO1Element.NONE, EO1Element.NONE, EO1Ailment.FEAR, EO1SkillNeed.HEAD, EO1SkillMastery.CURSE, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[8,9,10,11,12,12,12,12,12,12]),EO1SkillValue(EO1SkillValueType.EFFICACY_SUCCESS_RATE,[50,51,52,53,59,60,61,62,63,70]),EO1SkillValue(EO1SkillValueType.SPEED,[50,50,50,50,50,50,50,50,50,50])]),
    EO1SkillData(EO1Skills.HEXER_SUICIDE, "Suicide", 384, "Hexer", 18, EO1SkillType.SPECIAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.CURSE, EO1SkillTarget.ONE, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[10,11,12,13,14,14,14,14,14,14]),EO1SkillValue(EO1SkillValueType.ATTACK_NUMBER,[1,1,2,2,3,3,3,3,3,4])]),
    EO1SkillData(EO1Skills.HEXER_BETRAYAL, "Betrayal", 385, "Hexer", 17, EO1SkillType.SPECIAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.CURSE, EO1SkillTarget.ALL, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[10,9,8,7,6,5,4,3,2,1])]),
    EO1SkillData(EO1Skills.HEXER_PARALYZE, "Paralyze", 386, "Hexer", 16, EO1SkillType.SPECIAL, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.CURSE, EO1SkillTarget.ALL, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[10,9,8,7,6,5,4,3,2,1])]),
    EO1SkillData(EO1Skills.HEXER_REVENGE, "Revenge", 387, "Hexer", 14, EO1SkillType.SPECIAL, EO1Element.BASH, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.HEAD, EO1SkillMastery.CURSE, EO1SkillTarget.ALL, EO1SkillSide.OTHER, EO1SkillUsage.BATTLE, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[6,7,8,9,10,10,10,10,10,10]),EO1SkillValue(EO1SkillValueType.SKILL_COEFFICIENT,[100,102,104,106,120,122,124,126,128,150]),EO1SkillValue(EO1SkillValueType.SPEED,[50,50,50,50,50,50,50,50,50,50]),EO1SkillValue(EO1SkillValueType.HIT_RATE,[100,100,100,100,100,100,100,100,100,100])]),
    EO1SkillData(EO1Skills.HEXER_LURE, "Lure", 388, "Hexer", 19, EO1SkillType.PASSIVE, EO1Element.NONE, EO1Element.NONE, EO1Ailment.NONE, EO1SkillNeed.NONE, EO1SkillMastery.NONE, EO1SkillTarget.ALL, EO1SkillSide.SELF, EO1SkillUsage.DUNGEON, EO1SkillEffect.ATTACK, [EO1SkillValue(EO1SkillValueType.CONSUMPTION_TP,[2,2,3,3,4,4,4,4,4,4]),EO1SkillValue(EO1SkillValueType.TURN_NUMBER,[16,18,20,22,30,32,34,36,38,50]),EO1SkillValue(EO1SkillValueType.RATE_X1,[130,130,130,130,130,135,135,140,145,150])]),
]

ALL_SKILLS_DATA: list[EO1SkillData] = [
    *LANDSKNECHT_SKILLS,
    *SURVIVALIST_SKILLS,
    *PROTECTOR_SKILLS,
    *DARK_HUNTER_SKILLS,
    *MEDIC_SKILLS,
    *ALCHEMIST_SKILLS,
    *TROUBADOUR_SKILLS,
    *RONIN_SKILLS,
    *HEXER_SKILLS,
]

SKILL_DATA_BY_ID: dict[int, EO1SkillData] = {skill_data.id:skill_data for skill_data in ALL_SKILLS_DATA}
SKILL_DATA_BY_ITEM_ID: dict[int, EO1SkillData] = {skill_data.ap_item_id:skill_data for skill_data in ALL_SKILLS_DATA}