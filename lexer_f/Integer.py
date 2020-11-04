from .Token import *
from .Tag import *


class Integer(Token):
    def __init__(self, value):
        super().__init__(Tag.INTEGER)
        self.value = value

    def getValue(self):
        return self.value

    def toString(self):
        return "INTEGER - VALUE = " + str(self.value)
