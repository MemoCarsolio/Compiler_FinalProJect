from .Token import *
from .Tag import *


class CharacterString(Token):
    def __init__(self, value):
        super().__init__(Tag.CHARACTERSTRING)
        self.value = value

    def getValue(self):
        return self.value

    def toString(self):
        return "string"
