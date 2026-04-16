from .Bases import EtrianOdysseyTestBase
from .Constant import *
from ..Constant import *

class DefaultOptionsTest(EtrianOdysseyTestBase):
    options = {
        OptionKeys.GOAL: EO1Goal.defeat_etreant.value,
    }
