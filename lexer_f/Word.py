from .Token import *
from .Tag import *


class Word(Token):
    def __init__(self, lexeme, tag):
        super().__init__(tag)
        self.lexeme = lexeme

    def getLexeme(self):
        return str(self.lexeme)

    def toString(self):
        return self.lexeme


eq = Word("==", Tag.EQ)
ne = Word("<>", Tag.NEQ)
le = Word("<=", Tag.LE)
ge = Word(">=", Tag.GE)
minus = Word("minus", Tag.MINUS)
assign = Word(":=", Tag.ASSIGN)
true = Word("true", Tag.TRUE)
false = Word("false", Tag.FALSE)

prewords = [eq, ne, le, ge, minus, assign, true, false]
