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
        if self.token.getTag() == tag:
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

    def program_block(self):
        aux = self.constant_declaration_part()
        aux = aux + self.variable_declaration_part()
        return aux + self.statement_part()

    def opt_program_parameters(self):
        if str(self.token.getTag()) == "(":
            check("(")
            aux = self.program_parameters()
            if str(self.token.getTag()) == ")":
                check(")")
                return "( " + aux + " )"
        else:
            return ""

    def constant_declaration_part(self):
        if self.token.getTag() == 257:
            check(257)
            aux = "constant " + self.constant_definition()
            check(";")
            return aux + "; " + self.more_constant_definition()
        else:
            return ""

    def variable_declaration_part(self):
        if self.token.getTag() == 258:
            check(258)
            aux = "var " + self.variable_declaration()
            check(";")
            return aux + "; " + self.more_variable_declaration()
        else:
            return ""

    def statement_part(self):
        check(259)
        aux = "begin " + self.statement_sequence()
        check(260)
        return aux + " end"

    def program_parameters(self):
        return self.identifier_list()

    def constant_definition(self):
        check(290)
        check("=")
        return "id = " + self.expression()

    def more_constant_definition(self):
        if self.token.getTag() == 290:

            aux = self.constant_definition()
            check(";")
            return aux + "; " + self.more_constant_definition()
        else:
            return ""

    def variable_declaration(self):
        aux = self.identifier_list()
        check(":")
        return aux + ": " + self.type()

    def more_variable_declaration(self):
        if self.token.getTag() == 290:
            aux = self.variable_declaration()
            check(";")
            return aux + "; " + self.more_variable_declaration()
        else:
            return ""

    def statement_sequence(self):
        aux = self.statement()
        check(";")
        return aux + "; " + self.more_statement()

    def identifier_list(self):
        check(290)
        return "id " + self.more_identifier()

    def expression(self):
        aux = self.simple_expression()
        return aux + " " + self.opt_rel_expression()

    def statement(self):

        pass
