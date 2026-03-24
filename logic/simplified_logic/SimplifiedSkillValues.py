from __future__ import annotations
from enum import StrEnum, IntEnum
from dataclasses import dataclass
from abc import ABC, abstractmethod

from worlds.stardew_valley.strings.ap_names.mods.mod_items import SkillLevel
from ...data.Generic import *
from ...data.SkillData import *
from .Constant import *

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

class SkillUseType(IntEnum):
    NON_BATTLE = 0
    PASSIVE = 1
    ACTIVE = 2

@dataclass
class SimplifiedSkillValues(ABC):
    skill_id: int

    #def __init__(self, skill_id: int, viability_level: SkillViabilityLevel):
    #    self.skill_id = skill_id

    @abstractmethod
    def get_skill_use_type(self) -> SkillUseType:
        pass

    @abstractmethod
    def get_skill_type(self) -> SkillType:
        pass

@dataclass
class NonBattleSkillValues(SimplifiedSkillValues):
    def get_skill_use_type(self) -> SkillUseType:
        return SkillUseType.NON_BATTLE
    def get_skill_type(self) -> SkillType:
        return SkillType.NON_BATTLE

@dataclass
class PassiveSkillValues(SimplifiedSkillValues):
    def get_skill_use_type(self) -> SkillUseType:
        return SkillUseType.PASSIVE
    @abstractmethod
    def get_skill_type(self) -> SkillType:
        pass

@dataclass
class ActiveSkillValues(SimplifiedSkillValues):
    viability_level: SkillViabilityLevel

    def get_skill_use_type(self) -> SkillUseType:
        return SkillUseType.ACTIVE
    @abstractmethod
    def get_skill_type(self) -> SkillType:
        pass
    @abstractmethod
    def is_offensive_skill(self) -> bool:
        pass


@dataclass
class PassiveStatSkillValues(PassiveSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.PASSIVE_STAT

class AttackSkillValues(ActiveSkillValues):
    #skill_power: SkillPower
    #primary_element: EO1Element
    #secondary_element: EO1Element
    #is_magical: bool
    def is_offensive_skill(self) -> bool:
        return True
    def get_skill_type(self) -> SkillType:
        return SkillType.ATTACK

class MasterySkillValues(PassiveSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.MASTERY

class NormalAttackPassiveSkillValues(PassiveSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.NORMAL_ATTACK_PASSIVE

class BuffSkillValues(ActiveSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.BUFF
    def is_offensive_skill(self) -> bool:
        return False

class HealSkillValues(ActiveSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.HEAL
    def is_offensive_skill(self) -> bool:
        return False

class EscapeSkillValues(ActiveSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.ESCAPE
    def is_offensive_skill(self) -> bool:
        return False

class ChaseSkillValues(ActiveSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.CHASE
    def is_offensive_skill(self) -> bool:
        return True

class DebuffSkillValues(ActiveSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.DEBUFF
    def is_offensive_skill(self) -> bool:
        return False

class AggroSkillValues(ActiveSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.AGGRO
    def is_offensive_skill(self) -> bool:
        return False

class TurnManipulationSkillValues(ActiveSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.TURN_MANIPULATION
    def is_offensive_skill(self) -> bool:
        return False

class TurnManipulationPassiveSkillValues(PassiveSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.TURN_MANIPULATION

class BattleStartPassiveSkillValues(PassiveSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.BATTLE_START_PASSIVE

class AilmentHealValues(ActiveSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.AILMENT_HEAL
    def is_offensive_skill(self) -> bool:
        return False

class PassiveBoostValues(PassiveSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.PASSIVE_BOOST

class AilmentAttackValues(ActiveSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.AILMENT_ATTACK
    def is_offensive_skill(self) -> bool:
        return False#??

class GuardSkillValues(ActiveSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.GUARD
    def is_offensive_skill(self) -> bool:
        return False

class CounterSkillValues(ActiveSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.COUNTER
    def is_offensive_skill(self) -> bool:
        return True

class ReviveSkillValues(ActiveSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.REVIVE
    def is_offensive_skill(self) -> bool:
        return False

class BuffRemovalSkillValues(ActiveSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.BUFF_REMOVAL
    def is_offensive_skill(self) -> bool:
        return False

class CurseSkillValues(ActiveSkillValues):
    def get_skill_type(self) -> SkillType:
        return SkillType.CURSE
    def is_offensive_skill(self) -> bool:
        return False#??



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
    BuffSkillValues(EO1Skills.LANDSKNECHT_WAR_CRY, SkillViabilityLevel.NORMAL),
    BuffSkillValues(EO1Skills.LANDSKNECHT_HELL_CRY, SkillViabilityLevel.GOOD),
    AilmentHealValues(EO1Skills.LANDSKNECHT_ARM_HEAL, SkillViabilityLevel.BAD),
    AttackSkillValues(EO1Skills.LANDSKNECHT_CRUSH, SkillViabilityLevel.GOOD),
    AttackSkillValues(EO1Skills.LANDSKNECHT_STUNNER, SkillViabilityLevel.NORMAL),
    AttackSkillValues(EO1Skills.LANDSKNECHT_SILENCER, SkillViabilityLevel.NORMAL),
    AttackSkillValues(EO1Skills.LANDSKNECHT_CLEAVER, SkillViabilityLevel.NORMAL),
    AttackSkillValues(EO1Skills.LANDSKNECHT_TORNADO, SkillViabilityLevel.NORMAL),
    AttackSkillValues(EO1Skills.LANDSKNECHT_ALLSLASH, SkillViabilityLevel.GOOD),
    ChaseSkillValues(EO1Skills.LANDSKNECHT_BLAZER, SkillViabilityLevel.SITUATIONAL),
    ChaseSkillValues(EO1Skills.LANDSKNECHT_SHOCKER, SkillViabilityLevel.SITUATIONAL),
    ChaseSkillValues(EO1Skills.LANDSKNECHT_FREEZER, SkillViabilityLevel.SITUATIONAL),
    EscapeSkillValues(EO1Skills.LANDSKNECHT_FLEE, SkillViabilityLevel.SITUATIONAL),

    # Survivalist
    PassiveStatSkillValues(EO1Skills.SURVIVALIST_HP_UP),
    PassiveStatSkillValues(EO1Skills.SURVIVALIST_TP_UP),
    PassiveStatSkillValues(EO1Skills.SURVIVALIST_AGI_UP),
    MasterySkillValues(EO1Skills.SURVIVALIST_BOWS),
    TurnManipulationPassiveSkillValues(EO1Skills.SURVIVALIST_1ST_HIT),
    BattleStartPassiveSkillValues(EO1Skills.SURVIVALIST_AMBUSH),
    NonBattleSkillValues(EO1Skills.SURVIVALIST_CHOP),
    NonBattleSkillValues(EO1Skills.SURVIVALIST_MINE),
    NonBattleSkillValues(EO1Skills.SURVIVALIST_TAKE),
    TurnManipulationSkillValues(EO1Skills.SURVIVALIST_1ST_TURN, SkillViabilityLevel.GOOD),
    DebuffSkillValues(EO1Skills.SURVIVALIST_TRICKERY, SkillViabilityLevel.NORMAL),
    BuffSkillValues(EO1Skills.SURVIVALIST_QUICKEN, SkillViabilityLevel.BAD),
    AttackSkillValues(EO1Skills.SURVIVALIST_TRUESHOT, SkillViabilityLevel.NORMAL),
    AttackSkillValues(EO1Skills.SURVIVALIST_MULTIHIT, SkillViabilityLevel.GOOD),
    AttackSkillValues(EO1Skills.SURVIVALIST_DISABLE, SkillViabilityLevel.NORMAL),
    AttackSkillValues(EO1Skills.SURVIVALIST_APOLLON, SkillViabilityLevel.GOOD),
    AggroSkillValues(EO1Skills.SURVIVALIST_CLOAK, SkillViabilityLevel.TERRIBLE),
    EscapeSkillValues(EO1Skills.SURVIVALIST_ESCAPE, SkillViabilityLevel.SITUATIONAL),
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
    AggroSkillValues(EO1Skills.PROTECTOR_PROVOKE, SkillViabilityLevel.TERRIBLE),
    GuardSkillValues(EO1Skills.PROTECTOR_F_GUARD, SkillViabilityLevel.GOOD),
    GuardSkillValues(EO1Skills.PROTECTOR_B_GUARD, SkillViabilityLevel.BAD),
    GuardSkillValues(EO1Skills.PROTECTOR_PARRY, SkillViabilityLevel.NORMAL),
    BuffSkillValues(EO1Skills.PROTECTOR_FORTIFY, SkillViabilityLevel.NORMAL),
    BuffSkillValues(EO1Skills.PROTECTOR_DEFENDER, SkillViabilityLevel.GOOD),
    AttackSkillValues(EO1Skills.PROTECTOR_SMITE, SkillViabilityLevel.GOOD),
    GuardSkillValues(EO1Skills.PROTECTOR_ANTIFIRE, SkillViabilityLevel.SITUATIONAL),
    GuardSkillValues(EO1Skills.PROTECTOR_ANTIVOLT, SkillViabilityLevel.SITUATIONAL),
    GuardSkillValues(EO1Skills.PROTECTOR_ANTICOLD, SkillViabilityLevel.SITUATIONAL),
    HealSkillValues(EO1Skills.PROTECTOR_CURE, SkillViabilityLevel.NORMAL),
    HealSkillValues(EO1Skills.PROTECTOR_CURE_II, SkillViabilityLevel.NORMAL),
    EscapeSkillValues(EO1Skills.PROTECTOR_FLEE, SkillViabilityLevel.SITUATIONAL),
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
    AggroSkillValues(EO1Skills.DARK_HUNTER_CLOAK, SkillViabilityLevel.TERRIBLE),
    AttackSkillValues(EO1Skills.DARK_HUNTER_VIPER, SkillViabilityLevel.NORMAL),
    AttackSkillValues(EO1Skills.DARK_HUNTER_GAG, SkillViabilityLevel.NORMAL),
    AttackSkillValues(EO1Skills.DARK_HUNTER_CUFFS, SkillViabilityLevel.NORMAL),
    AttackSkillValues(EO1Skills.DARK_HUNTER_SHACKLES, SkillViabilityLevel.NORMAL),
    AttackSkillValues(EO1Skills.DARK_HUNTER_ECSTASY, SkillViabilityLevel.SITUATIONAL),
    AttackSkillValues(EO1Skills.DARK_HUNTER_CLIMAX, SkillViabilityLevel.SITUATIONAL),
    AttackSkillValues(EO1Skills.DARK_HUNTER_HYPNOS, SkillViabilityLevel.NORMAL),
    AttackSkillValues(EO1Skills.DARK_HUNTER_NERVE, SkillViabilityLevel.NORMAL),
    AttackSkillValues(EO1Skills.DARK_HUNTER_PETRIFY, SkillViabilityLevel.NORMAL),
    CounterSkillValues(EO1Skills.DARK_HUNTER_BAIT, SkillViabilityLevel.GOOD),
    AttackSkillValues(EO1Skills.DARK_HUNTER_DRAIN, SkillViabilityLevel.GOOD),
    AttackSkillValues(EO1Skills.DARK_HUNTER_MIRAGE, SkillViabilityLevel.NORMAL),

    # Medic
    PassiveStatSkillValues(EO1Skills.MEDIC_HP_UP),
    PassiveStatSkillValues(EO1Skills.MEDIC_TP_UP),
    PassiveStatSkillValues(EO1Skills.MEDIC_ATK_UP),
    MasterySkillValues(EO1Skills.MEDIC_HEALER),
    NonBattleSkillValues(EO1Skills.MEDIC_PATCH_UP),
    NonBattleSkillValues(EO1Skills.MEDIC_SCAVENGE),
    PassiveBoostValues(EO1Skills.MEDIC_TP_REGEN),
    NonBattleSkillValues(EO1Skills.MEDIC_CHOP),
    HealSkillValues(EO1Skills.MEDIC_CURE, SkillViabilityLevel.NORMAL),
    HealSkillValues(EO1Skills.MEDIC_CURE_II, SkillViabilityLevel.NORMAL),
    HealSkillValues(EO1Skills.MEDIC_CURE_III, SkillViabilityLevel.NORMAL),
    HealSkillValues(EO1Skills.MEDIC_SALVE, SkillViabilityLevel.NORMAL),
    HealSkillValues(EO1Skills.MEDIC_SALVE_II, SkillViabilityLevel.GOOD),
    ReviveSkillValues(EO1Skills.MEDIC_REVIVE, SkillViabilityLevel.GOOD),
    AilmentHealValues(EO1Skills.MEDIC_UNBIND, SkillViabilityLevel.SITUATIONAL),
    AilmentHealValues(EO1Skills.MEDIC_REFRESH, SkillViabilityLevel.SITUATIONAL),
    BuffSkillValues(EO1Skills.MEDIC_IMMUNIZE, SkillViabilityLevel.GOOD),
    AttackSkillValues(EO1Skills.MEDIC_CADUCEUS, SkillViabilityLevel.NORMAL),
    BuffSkillValues(EO1Skills.MEDIC_CPR, SkillViabilityLevel.BAD), # To validate if buff
    BuffSkillValues(EO1Skills.MEDIC_REGEN, SkillViabilityLevel.BAD),
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
    AttackSkillValues(EO1Skills.ALCHEMIST_FIRE, SkillViabilityLevel.NORMAL),
    AttackSkillValues(EO1Skills.ALCHEMIST_FLAME, SkillViabilityLevel.GOOD),
    AttackSkillValues(EO1Skills.ALCHEMIST_INFERNO, SkillViabilityLevel.GOOD),
    AttackSkillValues(EO1Skills.ALCHEMIST_ICE, SkillViabilityLevel.NORMAL),
    AttackSkillValues(EO1Skills.ALCHEMIST_FREEZE, SkillViabilityLevel.GOOD),
    AttackSkillValues(EO1Skills.ALCHEMIST_COCYTUS, SkillViabilityLevel.GOOD),
    AttackSkillValues(EO1Skills.ALCHEMIST_VOLT, SkillViabilityLevel.NORMAL),
    AttackSkillValues(EO1Skills.ALCHEMIST_THUNDER, SkillViabilityLevel.GOOD),
    AttackSkillValues(EO1Skills.ALCHEMIST_THOR, SkillViabilityLevel.GOOD),
    AilmentAttackValues(EO1Skills.ALCHEMIST_POISON, SkillViabilityLevel.NORMAL),
    AilmentAttackValues(EO1Skills.ALCHEMIST_VENOM, SkillViabilityLevel.NORMAL),
    NonBattleSkillValues(EO1Skills.ALCHEMIST_SIGHT),
    NonBattleSkillValues(EO1Skills.ALCHEMIST_WARP),

    # Troubadour
    PassiveStatSkillValues(EO1Skills.TROUBADOUR_HP_UP),
    PassiveStatSkillValues(EO1Skills.TROUBADOUR_TP_UP),
    MasterySkillValues(EO1Skills.TROUBADOUR_SONGS),
    NonBattleSkillValues(EO1Skills.TROUBADOUR_DIVINITY),
    BuffSkillValues(EO1Skills.TROUBADOUR_BRAVERY, SkillViabilityLevel.GOOD),
    BuffSkillValues(EO1Skills.TROUBADOUR_SHELTER, SkillViabilityLevel.NORMAL),
    BuffSkillValues(EO1Skills.TROUBADOUR_MERCURY, SkillViabilityLevel.BAD),
    BuffSkillValues(EO1Skills.TROUBADOUR_BLAZE, SkillViabilityLevel.SITUATIONAL),
    BuffSkillValues(EO1Skills.TROUBADOUR_FROST, SkillViabilityLevel.SITUATIONAL),
    BuffSkillValues(EO1Skills.TROUBADOUR_SHOCK, SkillViabilityLevel.SITUATIONAL),
    BuffRemovalSkillValues(EO1Skills.TROUBADOUR_ERASURE, SkillViabilityLevel.SITUATIONAL),
    BuffSkillValues(EO1Skills.TROUBADOUR_STAMINA, SkillViabilityLevel.NORMAL),
    BuffSkillValues(EO1Skills.TROUBADOUR_IFRIT, SkillViabilityLevel.SITUATIONAL),
    BuffSkillValues(EO1Skills.TROUBADOUR_YMIR, SkillViabilityLevel.SITUATIONAL),
    BuffSkillValues(EO1Skills.TROUBADOUR_TARANIS, SkillViabilityLevel.SITUATIONAL),
    BuffSkillValues(EO1Skills.TROUBADOUR_HEALING, SkillViabilityLevel.NORMAL), # Bad?
    BuffSkillValues(EO1Skills.TROUBADOUR_RELAXING, SkillViabilityLevel.GOOD),
    BuffSkillValues(EO1Skills.TROUBADOUR_RECOVERY, SkillViabilityLevel.SITUATIONAL),
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
    HealSkillValues(EO1Skills.RONIN_IBUKI, SkillViabilityLevel.NORMAL),
    AttackSkillValues(EO1Skills.RONIN_KESAGIRI, SkillViabilityLevel.NORMAL),
    BuffSkillValues(EO1Skills.RONIN_OVERHEAD, SkillViabilityLevel.NORMAL),
    AttackSkillValues(EO1Skills.RONIN_ZAMBA, SkillViabilityLevel.NORMAL),
    AttackSkillValues(EO1Skills.RONIN_MIDAREBA, SkillViabilityLevel.GOOD),
    AttackSkillValues(EO1Skills.RONIN_OROCHI, SkillViabilityLevel.NORMAL),
    BuffSkillValues(EO1Skills.RONIN_SEIGAN, SkillViabilityLevel.NORMAL),
    GuardSkillValues(EO1Skills.RONIN_MIKIRI, SkillViabilityLevel.NORMAL),
    AttackSkillValues(EO1Skills.RONIN_KOTEUCHI, SkillViabilityLevel.NORMAL),
    AttackSkillValues(EO1Skills.RONIN_RAIZUKI, SkillViabilityLevel.NORMAL),
    BuffSkillValues(EO1Skills.RONIN_IAI, SkillViabilityLevel.BAD),
    AttackSkillValues(EO1Skills.RONIN_KUBIUCHI, SkillViabilityLevel.NORMAL),
    AttackSkillValues(EO1Skills.RONIN_GATOTSU, SkillViabilityLevel.GOOD),
    AttackSkillValues(EO1Skills.RONIN_HYOSETSU, SkillViabilityLevel.NORMAL),

    # Hexer
    PassiveStatSkillValues(EO1Skills.HEXER_HP_UP),
    PassiveStatSkillValues(EO1Skills.HEXER_TP_UP),
    MasterySkillValues(EO1Skills.HEXER_CURSES),
    BattleStartPassiveSkillValues(EO1Skills.HEXER_STAGGER),
    NonBattleSkillValues(EO1Skills.HEXER_MINE),
    DebuffSkillValues(EO1Skills.HEXER_SAPPING, SkillViabilityLevel.GOOD),
    DebuffSkillValues(EO1Skills.HEXER_FRAILTY, SkillViabilityLevel.GOOD),
    DebuffSkillValues(EO1Skills.HEXER_LEADEN, SkillViabilityLevel.BAD),
    CurseSkillValues(EO1Skills.HEXER_RELAPSE, SkillViabilityLevel.SITUATIONAL),
    AilmentAttackValues(EO1Skills.HEXER_CRANIAL, SkillViabilityLevel.SITUATIONAL),
    AilmentAttackValues(EO1Skills.HEXER_ABDOMEN, SkillViabilityLevel.SITUATIONAL),
    AilmentAttackValues(EO1Skills.HEXER_IMMOBILE, SkillViabilityLevel.SITUATIONAL),
    AilmentAttackValues(EO1Skills.HEXER_BLINDING, SkillViabilityLevel.NORMAL),
    AilmentAttackValues(EO1Skills.HEXER_TORPOR, SkillViabilityLevel.NORMAL),
    AilmentAttackValues(EO1Skills.HEXER_CORRUPT, SkillViabilityLevel.SITUATIONAL),
    AilmentAttackValues(EO1Skills.HEXER_EVIL_EYE, SkillViabilityLevel.SITUATIONAL),
    CurseSkillValues(EO1Skills.HEXER_SUICIDE, SkillViabilityLevel.NORMAL),
    CurseSkillValues(EO1Skills.HEXER_BETRAYAL, SkillViabilityLevel.NORMAL),
    CurseSkillValues(EO1Skills.HEXER_PARALYZE, SkillViabilityLevel.BAD),
    AttackSkillValues(EO1Skills.HEXER_REVENGE, SkillViabilityLevel.BAD),
    NonBattleSkillValues(EO1Skills.HEXER_LURE),
]

SIMPLIFIED_SKILL_BY_SKILL_ID: dict[int, SimplifiedSkillValues] = {skill_value.skill_id: skill_value for skill_value in SIMPLIFIED_SKILL_VALUES}


