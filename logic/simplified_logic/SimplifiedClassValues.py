from dataclasses import dataclass, field
from ...data.ClassData import EO1Class
from ...data.SkillData import EO1Skills


@dataclass
class SimplifiedClassValues:
    class_name: str
    is_front_row_viable: bool
    is_back_row_viable: bool
    non_cumulative_logic_skills: set[int] = field(default_factory=set)

SIMPLIFIED_CLASS_VALUES_TABLE: list[SimplifiedClassValues] = [
    SimplifiedClassValues(EO1Class.LANDSKNECHT, is_front_row_viable=True, is_back_row_viable=False),
    SimplifiedClassValues(EO1Class.SURVIVALIST, is_front_row_viable=False, is_back_row_viable=True),
    SimplifiedClassValues(EO1Class.PROTECTOR, is_front_row_viable=True, is_back_row_viable=False),
    SimplifiedClassValues(EO1Class.DARK_HUNTER, is_front_row_viable=True, is_back_row_viable=False),
    SimplifiedClassValues(EO1Class.MEDIC, is_front_row_viable=False, is_back_row_viable=True),
    SimplifiedClassValues(EO1Class.ALCHEMIST, is_front_row_viable=False, is_back_row_viable=True),
    SimplifiedClassValues(EO1Class.TROUBADOUR, is_front_row_viable=False, is_back_row_viable=True),
    SimplifiedClassValues(EO1Class.RONIN, is_front_row_viable=True, is_back_row_viable=False,
                          non_cumulative_logic_skills={EO1Skills.RONIN_OVERHEAD, EO1Skills.RONIN_IAI, EO1Skills.RONIN_SEIGAN }),
    SimplifiedClassValues(EO1Class.HEXER, is_front_row_viable=False, is_back_row_viable=True,
                          non_cumulative_logic_skills={EO1Skills.HEXER_SUICIDE, EO1Skills.HEXER_BETRAYAL, EO1Skills.HEXER_PARALYZE }),
]

SIMPLIFIED_CLASS_VALUES_BY_NAME: dict[str, SimplifiedClassValues] = {class_data.class_name:class_data for class_data in SIMPLIFIED_CLASS_VALUES_TABLE}
