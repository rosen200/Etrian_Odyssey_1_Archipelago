from enum import StrEnum, IntEnum
from dataclasses import dataclass
from abc import ABC, abstractmethod

from ...data.Generic import *
from ...data.SkillData import *

class SkillPower(IntEnum):
    WEAK = 1
    MEDIUM = 2
    STRONG = 3

class SkillType(IntEnum):
    NON_BATTLE = 0
    ATTACK = 1
    NORMAL_ATTACK_PASSIVE = 4
    #MAGICAL_ATTACK = 2
    CHASE = 8
    COUNTER = 17
    AILMENT_ATTACK = 15
    PASSIVE_STAT = 2
    BATTLE_START_PASSIVE = 12
    PASSIVE_BOOST = 14
    MASTERY = 3
    GUARD = 16
    AGGRO = 10
    BUFF = 5
    DEBUFF = 9
    HEAL = 6
    AILMENT_HEAL = 13
    REVIVE = 18
    ESCAPE = 7
    TURN_MANIPULATION = 11
    BUFF_REMOVAL = 19
    CURSE = 20

class SimplifiedSkillValues(ABC):
    skill_id: int
    #class_name: str

    def __init__(self, skill_id: int):
        self.skill_id = skill_id

    @abstractmethod
    def get_skill_type(self) -> SkillType:
        pass

class NonBattleSkillValues(SimplifiedSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.NON_BATTLE

class AttackSkillValues(SimplifiedSkillValues):
    skill_power: SkillPower
    primary_element: EO1Element
    secondary_element: EO1Element
    is_magical: bool

    def get_skill_type(self) -> SkillType:
        return SkillType.ATTACK

class PassiveStatSkillValues(SimplifiedSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.PASSIVE_STAT

class MasterySkillValues(SimplifiedSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.MASTERY

class NormalAttackPassiveSkillValues(SimplifiedSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.NORMAL_ATTACK_PASSIVE

class BuffSkillValues(SimplifiedSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.BUFF

class HealSkillValues(SimplifiedSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.HEAL

class EscapeSkillValues(SimplifiedSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.ESCAPE

class ChaseSkillValues(SimplifiedSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.CHASE

class DebuffSkillValues(SimplifiedSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.DEBUFF

class AggroSkillValues(SimplifiedSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.AGGRO

class TurnManipulationSkillValues(SimplifiedSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.TURN_MANIPULATION

class BattleStartPassiveSkillValues(SimplifiedSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.BATTLE_START_PASSIVE

class AilmentHealValues(SimplifiedSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.AILMENT_HEAL

class PassiveBoostValues(SimplifiedSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.PASSIVE_BOOST

class AilmentAttackValues(SimplifiedSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.AILMENT_ATTACK

class GuardSkillValues(SimplifiedSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.GUARD

class CounterSkillValues(SimplifiedSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.COUNTER

class ReviveSkillValues(SimplifiedSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.REVIVE

class BuffRemovalSkillValues(SimplifiedSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.BUFF_REMOVAL

class CurseSkillValues(SimplifiedSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.CURSE











SIMPLIFIED_SKILL_VALUES: list[SimplifiedSkillValues] = [
    # Landsknecht
    PassiveStatSkillValues(EO1Skills.LANDSKNECHT_HP_UP),
    PassiveStatSkillValues(EO1Skills.LANDSKNECHT_TP_UP),
    PassiveStatSkillValues(EO1Skills.LANDSKNECHT_ATK_UP),
    PassiveStatSkillValues(EO1Skills.LANDSKNECHT_DEF_UP),
    MasterySkillValues(EO1Skills.LANDSKNECHT_AXES),
    MasterySkillValues(EO1Skills.LANDSKNECHT_SWORDS),
    NormalAttackPassiveSkillValues(EO1Skills.LANDSKNECHT_2_HIT),
    NonBattleSkillValues(EO1Skills.LANDSKNECHT_MINE),
    BuffSkillValues(EO1Skills.LANDSKNECHT_WAR_CRY),
    BuffSkillValues(EO1Skills.LANDSKNECHT_HELL_CRY),
    AilmentHealValues(EO1Skills.LANDSKNECHT_ARM_HEAL),
    AttackSkillValues(EO1Skills.LANDSKNECHT_CRUSH),
    AttackSkillValues(EO1Skills.LANDSKNECHT_STUNNER),
    AttackSkillValues(EO1Skills.LANDSKNECHT_SILENCER),
    AttackSkillValues(EO1Skills.LANDSKNECHT_CLEAVER),
    AttackSkillValues(EO1Skills.LANDSKNECHT_TORNADO),
    AttackSkillValues(EO1Skills.LANDSKNECHT_ALLSLASH),
    ChaseSkillValues(EO1Skills.LANDSKNECHT_BLAZER),
    ChaseSkillValues(EO1Skills.LANDSKNECHT_SHOCKER),
    ChaseSkillValues(EO1Skills.LANDSKNECHT_FREEZER),
    EscapeSkillValues(EO1Skills.LANDSKNECHT_FLEE),

    # Survivalist
    PassiveStatSkillValues(EO1Skills.SURVIVALIST_HP_UP),
    PassiveStatSkillValues(EO1Skills.SURVIVALIST_TP_UP),
    PassiveStatSkillValues(EO1Skills.SURVIVALIST_AGI_UP),
    MasterySkillValues(EO1Skills.SURVIVALIST_BOWS),
    TurnManipulationSkillValues(EO1Skills.SURVIVALIST_1ST_HIT),
    BattleStartPassiveSkillValues(EO1Skills.SURVIVALIST_AMBUSH),
    NonBattleSkillValues(EO1Skills.SURVIVALIST_CHOP),
    NonBattleSkillValues(EO1Skills.SURVIVALIST_MINE),
    NonBattleSkillValues(EO1Skills.SURVIVALIST_TAKE),
    TurnManipulationSkillValues(EO1Skills.SURVIVALIST_1ST_TURN),
    DebuffSkillValues(EO1Skills.SURVIVALIST_TRICKERY),
    BuffSkillValues(EO1Skills.SURVIVALIST_QUICKEN),
    AttackSkillValues(EO1Skills.SURVIVALIST_TRUESHOT),
    AttackSkillValues(EO1Skills.SURVIVALIST_MULTIHIT),
    AttackSkillValues(EO1Skills.SURVIVALIST_DISABLE),
    AttackSkillValues(EO1Skills.SURVIVALIST_APOLLON),
    AggroSkillValues(EO1Skills.SURVIVALIST_CLOAK),
    EscapeSkillValues(EO1Skills.SURVIVALIST_ESCAPE),
    BattleStartPassiveSkillValues(EO1Skills.SURVIVALIST_AWARE),
    NonBattleSkillValues(EO1Skills.SURVIVALIST_STALKER),
    NonBattleSkillValues(EO1Skills.SURVIVALIST_OWL_EYE),

    # Protector
    PassiveStatSkillValues(EO1Skills.PROTECTOR_HP_UP),
    PassiveStatSkillValues(EO1Skills.PROTECTOR_TP_UP),
    PassiveStatSkillValues(EO1Skills.PROTECTOR_DEF_UP),
    MasterySkillValues(EO1Skills.PROTECTOR_SHIELDS),
    PassiveBoostValues(EO1Skills.PROTECTOR_AEGIS),
    PassiveBoostValues(EO1Skills.PROTECTOR_EN_GARDE),
    NonBattleSkillValues(EO1Skills.PROTECTOR_MINE),
    AggroSkillValues(EO1Skills.PROTECTOR_PROVOKE),
    GuardSkillValues(EO1Skills.PROTECTOR_F_GUARD),
    GuardSkillValues(EO1Skills.PROTECTOR_B_GUARD),
    GuardSkillValues(EO1Skills.PROTECTOR_PARRY),
    BuffSkillValues(EO1Skills.PROTECTOR_FORTIFY),
    BuffSkillValues(EO1Skills.PROTECTOR_DEFENDER),
    AttackSkillValues(EO1Skills.PROTECTOR_SMITE),
    GuardSkillValues(EO1Skills.PROTECTOR_ANTIFIRE),
    GuardSkillValues(EO1Skills.PROTECTOR_ANTIVOLT),
    GuardSkillValues(EO1Skills.PROTECTOR_ANTICOLD),
    HealSkillValues(EO1Skills.PROTECTOR_CURE),
    HealSkillValues(EO1Skills.PROTECTOR_CURE_II),
    EscapeSkillValues(EO1Skills.PROTECTOR_FLEE),
    NonBattleSkillValues(EO1Skills.PROTECTOR_STALKER),

    # Dark Hunter
    PassiveStatSkillValues(EO1Skills.DARK_HUNTER_HP_UP),
    PassiveStatSkillValues(EO1Skills.DARK_HUNTER_TP_UP),
    PassiveStatSkillValues(EO1Skills.DARK_HUNTER_ATK_UP),
    MasterySkillValues(EO1Skills.DARK_HUNTER_WHIPS),
    MasterySkillValues(EO1Skills.DARK_HUNTER_SWORDS),
    PassiveBoostValues(EO1Skills.DARK_HUNTER_BOOST_UP),
    PassiveBoostValues(EO1Skills.DARK_HUNTER_FURY),
    NonBattleSkillValues(EO1Skills.DARK_HUNTER_TAKE),
    AggroSkillValues(EO1Skills.DARK_HUNTER_CLOAK),
    AttackSkillValues(EO1Skills.DARK_HUNTER_VIPER),
    AttackSkillValues(EO1Skills.DARK_HUNTER_GAG),
    AttackSkillValues(EO1Skills.DARK_HUNTER_CUFFS),
    AttackSkillValues(EO1Skills.DARK_HUNTER_SHACKLES),
    AttackSkillValues(EO1Skills.DARK_HUNTER_ECSTASY),
    AttackSkillValues(EO1Skills.DARK_HUNTER_CLIMAX),
    AttackSkillValues(EO1Skills.DARK_HUNTER_HYPNOS),
    AttackSkillValues(EO1Skills.DARK_HUNTER_NERVE),
    AttackSkillValues(EO1Skills.DARK_HUNTER_PETRIFY),
    CounterSkillValues(EO1Skills.DARK_HUNTER_BAIT),
    AttackSkillValues(EO1Skills.DARK_HUNTER_DRAIN),
    AttackSkillValues(EO1Skills.DARK_HUNTER_MIRAGE),

    # Medic
    PassiveStatSkillValues(EO1Skills.MEDIC_HP_UP),
    PassiveStatSkillValues(EO1Skills.MEDIC_TP_UP),
    PassiveStatSkillValues(EO1Skills.MEDIC_ATK_UP),
    MasterySkillValues(EO1Skills.MEDIC_HEALER),
    NonBattleSkillValues(EO1Skills.MEDIC_PATCH_UP),
    NonBattleSkillValues(EO1Skills.MEDIC_SCAVENGE),
    PassiveBoostValues(EO1Skills.MEDIC_TP_REGEN),
    NonBattleSkillValues(EO1Skills.MEDIC_CHOP),
    HealSkillValues(EO1Skills.MEDIC_CURE),
    HealSkillValues(EO1Skills.MEDIC_CURE_II),
    HealSkillValues(EO1Skills.MEDIC_CURE_III),
    HealSkillValues(EO1Skills.MEDIC_SALVE),
    HealSkillValues(EO1Skills.MEDIC_SALVE_II),
    ReviveSkillValues(EO1Skills.MEDIC_REVIVE),
    AilmentHealValues(EO1Skills.MEDIC_UNBIND),
    AilmentHealValues(EO1Skills.MEDIC_REFRESH),
    BuffSkillValues(EO1Skills.MEDIC_IMMUNIZE),
    AttackSkillValues(EO1Skills.MEDIC_CADUCEUS),
    BuffSkillValues(EO1Skills.MEDIC_CPR), # To validate
    BuffSkillValues(EO1Skills.MEDIC_REGEN),
    NonBattleSkillValues(EO1Skills.MEDIC_H_TOUCH),

    # Alchemist
    PassiveStatSkillValues(EO1Skills.ALCHEMIST_TP_UP),
    MasterySkillValues(EO1Skills.ALCHEMIST_FIRE_UP),
    MasterySkillValues(EO1Skills.ALCHEMIST_ICE_UP),
    MasterySkillValues(EO1Skills.ALCHEMIST_VOLT_UP),
    MasterySkillValues(EO1Skills.ALCHEMIST_TOXINS),
    NonBattleSkillValues(EO1Skills.ALCHEMIST_SCAVENGE),
    PassiveBoostValues(EO1Skills.ALCHEMIST_TP_REGEN),
    NonBattleSkillValues(EO1Skills.ALCHEMIST_CHOP),
    AttackSkillValues(EO1Skills.ALCHEMIST_FIRE),
    AttackSkillValues(EO1Skills.ALCHEMIST_FLAME),
    AttackSkillValues(EO1Skills.ALCHEMIST_INFERNO),
    AttackSkillValues(EO1Skills.ALCHEMIST_ICE),
    AttackSkillValues(EO1Skills.ALCHEMIST_FREEZE),
    AttackSkillValues(EO1Skills.ALCHEMIST_COCYTUS),
    AttackSkillValues(EO1Skills.ALCHEMIST_VOLT),
    AttackSkillValues(EO1Skills.ALCHEMIST_THUNDER),
    AttackSkillValues(EO1Skills.ALCHEMIST_THOR),
    AilmentAttackValues(EO1Skills.ALCHEMIST_POISON),
    AilmentAttackValues(EO1Skills.ALCHEMIST_VENOM),
    NonBattleSkillValues(EO1Skills.ALCHEMIST_SIGHT),
    NonBattleSkillValues(EO1Skills.ALCHEMIST_WARP),

    # Troubadour
    PassiveStatSkillValues(EO1Skills.TROUBADOUR_HP_UP),
    PassiveStatSkillValues(EO1Skills.TROUBADOUR_TP_UP),
    MasterySkillValues(EO1Skills.TROUBADOUR_SONGS),
    NonBattleSkillValues(EO1Skills.TROUBADOUR_DIVINITY),
    BuffSkillValues(EO1Skills.TROUBADOUR_BRAVERY),
    BuffSkillValues(EO1Skills.TROUBADOUR_SHELTER),
    BuffSkillValues(EO1Skills.TROUBADOUR_MERCURY),
    BuffSkillValues(EO1Skills.TROUBADOUR_BLAZE),
    BuffSkillValues(EO1Skills.TROUBADOUR_FROST),
    BuffSkillValues(EO1Skills.TROUBADOUR_SHOCK),
    BuffRemovalSkillValues(EO1Skills.TROUBADOUR_ERASURE),
    BuffSkillValues(EO1Skills.TROUBADOUR_STAMINA),
    BuffSkillValues(EO1Skills.TROUBADOUR_IFRIT),
    BuffSkillValues(EO1Skills.TROUBADOUR_YMIR),
    BuffSkillValues(EO1Skills.TROUBADOUR_TARANIS),
    BuffSkillValues(EO1Skills.TROUBADOUR_HEALING),
    BuffSkillValues(EO1Skills.TROUBADOUR_RELAXING),
    BuffSkillValues(EO1Skills.TROUBADOUR_RECOVERY),
    NonBattleSkillValues(EO1Skills.TROUBADOUR_STALKER),
    NonBattleSkillValues(EO1Skills.TROUBADOUR_RETURN),
    NonBattleSkillValues(EO1Skills.TROUBADOUR_TAKE),

    # Ronin
    PassiveStatSkillValues(EO1Skills.RONIN_HP_UP),
    PassiveStatSkillValues(EO1Skills.RONIN_TP_UP),
    PassiveStatSkillValues(EO1Skills.RONIN_ATK_UP),
    MasterySkillValues(EO1Skills.RONIN_KATANAS),
    NormalAttackPassiveSkillValues(EO1Skills.RONIN_CRIT_UP),
    PassiveBoostValues(EO1Skills.RONIN_SIGHT),
    NonBattleSkillValues(EO1Skills.RONIN_MINE),
    HealSkillValues(EO1Skills.RONIN_IBUKI),
    AttackSkillValues(EO1Skills.RONIN_KESAGIRI),
    BuffSkillValues(EO1Skills.RONIN_OVERHEAD),
    AttackSkillValues(EO1Skills.RONIN_ZAMBA),
    AttackSkillValues(EO1Skills.RONIN_MIDAREBA),
    AttackSkillValues(EO1Skills.RONIN_OROCHI),
    BuffSkillValues(EO1Skills.RONIN_SEIGAN),
    GuardSkillValues(EO1Skills.RONIN_MIKIRI),
    AttackSkillValues(EO1Skills.RONIN_KOTEUCHI),
    AttackSkillValues(EO1Skills.RONIN_RAIZUKI),
    BuffSkillValues(EO1Skills.RONIN_IAI),
    AttackSkillValues(EO1Skills.RONIN_KUBIUCHI),
    AttackSkillValues(EO1Skills.RONIN_GATOTSU),
    AttackSkillValues(EO1Skills.RONIN_HYOSETSU),

    # Hexer
    PassiveStatSkillValues(EO1Skills.HEXER_HP_UP),
    PassiveStatSkillValues(EO1Skills.HEXER_TP_UP),
    MasterySkillValues(EO1Skills.HEXER_CURSES),
    BattleStartPassiveSkillValues(EO1Skills.HEXER_STAGGER),
    NonBattleSkillValues(EO1Skills.HEXER_MINE),
    DebuffSkillValues(EO1Skills.HEXER_SAPPING),
    DebuffSkillValues(EO1Skills.HEXER_FRAILTY),
    DebuffSkillValues(EO1Skills.HEXER_LEADEN),
    CurseSkillValues(EO1Skills.HEXER_RELAPSE),
    AilmentAttackValues(EO1Skills.HEXER_CRANIAL),
    AilmentAttackValues(EO1Skills.HEXER_ABDOMEN),
    AilmentAttackValues(EO1Skills.HEXER_IMMOBILE),
    AilmentAttackValues(EO1Skills.HEXER_BLINDING),
    AilmentAttackValues(EO1Skills.HEXER_TORPOR),
    AilmentAttackValues(EO1Skills.HEXER_CORRUPT),
    AilmentAttackValues(EO1Skills.HEXER_EVIL_EYE),
    CurseSkillValues(EO1Skills.HEXER_SUICIDE),
    CurseSkillValues(EO1Skills.HEXER_BETRAYAL),
    CurseSkillValues(EO1Skills.HEXER_PARALYZE),
    AttackSkillValues(EO1Skills.HEXER_REVENGE),
    NonBattleSkillValues(EO1Skills.HEXER_LURE),
]

SIMPLIFIED_SKILL_BY_SKILL_ID: dict[int, SimplifiedSkillValues] = {skill_value.skill_id: skill_value for skill_value in SIMPLIFIED_SKILL_VALUES}


