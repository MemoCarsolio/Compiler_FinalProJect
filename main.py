from lexer_f import *
from parser_f import *
import sys


if len(sys.argv) != 2:
    print("usage: main.py file")
else:

    par = Parser(sys.argv[1])

    par.parse()


# par = Parser("test_cases/Example1.pas")
# par.analize()
# par.check()
