from lexer_f import *

class Parser:
    """docstring for ."""

    def __init__(self, input):
        self.lex = Lexer(input)
        self.token = ""
        pass

    def analize(self):
        self.token = self.lex.scan()
        aux = FUNC
        print()
        pass
