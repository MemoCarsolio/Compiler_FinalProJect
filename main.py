from lexer import *



x = Lexer("text.txt")



text = []

stuff = x.file.read()

for ch in stuff:
    text.append(ch)
print(text)
