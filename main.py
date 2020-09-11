from lexer import *
import sys



if len(sys.argv) != 2:
    print("usage: main.py file")
else:
    lex = Lexer(sys.argv[1])

    while True:
        aux = lex.scan()
        
        if aux.getTag() == 65535:
            print("Token = E0F")
            break
        print(aux.toString())
