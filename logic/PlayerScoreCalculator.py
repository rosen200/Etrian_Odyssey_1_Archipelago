from dataclasses import dataclass

from ..data.Generic import *

@dataclass
class SkillPowerScore:
    power_score: int
    primary_damage_type: EO1Element
    secondary_damage_type: EO1Element
    ailment: EO1Ailment



@dataclass
class PowerScores:
    slash_score: int
    bash_score: int
    stab_score: int
    fire_score: int
    ice_score: int
    thunder_score: int

@dataclass
class ToughnessScores:
    toughness_score: int


@dataclass
class ClassScores:
    power_scores: PowerScores
    toughness_scores: ToughnessScores

@dataclass
class PlayerAllScores:
    landsknecht_score: ClassScores
    survivalist_score: ClassScores
    protector_score: ClassScores
    dark_hunter_score: ClassScores
    medic_score: ClassScores
    alchemist_score: ClassScores
    troubadour_score: ClassScores
    ronin_score: ClassScores
    hexer_score: ClassScores