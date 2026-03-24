from dataclasses import dataclass
from ...data.ClassData import EO1Class

@dataclass
class SimplifiedClassValues:
    class_name: str
    is_front_row_viable: bool
    is_back_row_viable: bool

SIMPLIFIED_CLASS_VALUES_TABLE: list[SimplifiedClassValues] = [
    SimplifiedClassValues(EO1Class.LANDSKNECHT, is_front_row_viable=True, is_back_row_viable=False),
    SimplifiedClassValues(EO1Class.SURVIVALIST, is_front_row_viable=False, is_back_row_viable=True),
    SimplifiedClassValues(EO1Class.PROTECTOR, is_front_row_viable=True, is_back_row_viable=False),
    SimplifiedClassValues(EO1Class.DARK_HUNTER, is_front_row_viable=True, is_back_row_viable=False),
    SimplifiedClassValues(EO1Class.MEDIC, is_front_row_viable=False, is_back_row_viable=True),
    SimplifiedClassValues(EO1Class.ALCHEMIST, is_front_row_viable=False, is_back_row_viable=True),
    SimplifiedClassValues(EO1Class.TROUBADOUR, is_front_row_viable=False, is_back_row_viable=True),
    SimplifiedClassValues(EO1Class.RONIN, is_front_row_viable=True, is_back_row_viable=False),
    SimplifiedClassValues(EO1Class.HEXER, is_front_row_viable=False, is_back_row_viable=True),
]

SIMPLIFIED_CLASS_VALUES_BY_NAME: dict[str, SimplifiedClassValues] = {class_data.class_name:class_data for class_data in SIMPLIFIED_CLASS_VALUES_TABLE}
