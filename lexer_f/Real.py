from .Token import *
from .Tag import *


class Real(Token):
    def __init__(self, value):
        super().__init__(Tag.REAL)
        self.value = value

    def getValue(self):
        return self.value

    def toString(self):
        return "real"
