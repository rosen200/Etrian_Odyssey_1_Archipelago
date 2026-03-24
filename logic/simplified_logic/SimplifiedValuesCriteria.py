from __future__ import annotations
from dataclasses import dataclass, field
from abc import ABC, abstractmethod

from ...data.Generic import *

from .Constant import *

@dataclass
class SVCriteria(ABC):
    pass

@dataclass
class OrSVCriteria(SVCriteria):
    criteria: list[SVCriteria]

@dataclass
class AndSVCriteria(SVCriteria):
    criteria: list[SVCriteria]

@dataclass
class TrueSVCriteria(SVCriteria):
    pass

@dataclass
class ClassSVCriteria(SVCriteria):
    front_class_count: int | None = None
    back_class_count: int | None = None
    total_class_count: int | None = None
    criteria: SVCriteria = field(default_factory=TrueSVCriteria)

@dataclass
class CanUseDmgSkillSVCriteria(SVCriteria):
    instance_count: int = 1
    skill_power: SkillPower | None = None
    damage_type: EO1Element | None = None

@dataclass
class HasAntiStatusSVCriteria(SVCriteria):
    pass

@dataclass
class HasAntiBindSVCriteria(SVCriteria):
    pass

@dataclass
class CanInflictAilment(SVCriteria):
    ailment: EO1Ailment

@dataclass
class CanUseActiveSkill(SVCriteria):
    damage_type_resistances: list[EO1Element] = field(default_factory=list)
    ailment_resistances: list[EO1Ailment] = field(default_factory=list)
    skill_viability_level: SkillViabilityLevel | None = None
    skill_count: int = 1

