from lexer import *


lex = Lexer("text.txt")

print(lex.getReserved("<=").getLexeme())
