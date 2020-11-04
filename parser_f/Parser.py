from lexer_f import *

class Parser:
    """docstring for ."""

    def __init__(self, input):
        self.lex = Lexer(input)
        pass

    def analize(self):
        self.token = self.lex.scan()
        aux = start_p()
        print("ACCEPTED - Result = " + aux)
        pass
    def check(self, tag):
        if self.token.getTag == tag:
            self.token = self.lex.scan()
        else:
            raise Exception("you dumb")


    def start_p(self):
        return self.start()

    def start(self):
        aux = self.program_heading()
        check(";")
        aux = aux + "; " + self.program_block()
        check(".")
        return aux + "."

    def program_heading(self):
        check(256)
        check(290)
        return "program id " + self.opt_program_parameters()

        pass


    def program_block(self):

        pass
