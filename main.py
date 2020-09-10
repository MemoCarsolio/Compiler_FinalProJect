from lexer import *


lex = Lexer("text.txt")



test = [1,3,4,".",5,8]



print(lex.scan().getTag())
print(lex.scan().getTag())
print(lex.scan().getTag())
print(lex.scan().getTag())
print(lex.scan().getTag())
print(lex.scan().getTag())
print(lex.scan().getTag())
