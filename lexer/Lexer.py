from .Word import *
from .Tag import *
from .InputFile import *
from .Integer import *
from .Real import *
from .CharString import *

class Lexer:

    def __init__(self, filename):
        self.words = {}
        wordprep(prewords, self.words)
        reserve(Word("program",Tag.PROGRAM),self.words)
        reserve(Word("constant",Tag.CONSTANT),self.words)
        reserve(Word("var",Tag.VAR),self.words)
        reserve(Word("begin",Tag.BEGIN),self.words)
        reserve(Word("end",Tag.END),self.words)
        reserve(Word("integer",Tag.INTEGER),self.words)
        reserve(Word("real",Tag.REAL),self.words)
        reserve(Word("boolean",Tag.BOOLEAN),self.words)
        reserve(Word("string",Tag.STRING),self.words)
        reserve(Word("writeln",Tag.WRITELN),self.words)
        reserve(Word("readln",Tag.READLN),self.words)
        reserve(Word("while",Tag.WHILE),self.words)
        reserve(Word("do",Tag.DO),self.words)
        reserve(Word("repeat",Tag.REPEAT),self.words)
        reserve(Word("until",Tag.UNTIL),self.words)
        reserve(Word("for",Tag.FOR),self.words)
        reserve(Word("to",Tag.TO),self.words)
        reserve(Word("downto",Tag.DOWNTO),self.words)
        reserve(Word("if",Tag.IF),self.words)
        reserve(Word("then",Tag.THEN),self.words)
        reserve(Word("else",Tag.ELSE),self.words)
        reserve(Word("not",Tag.NOT),self.words)
        reserve(Word("div",Tag.DIV),self.words)
        reserve(Word("mod",Tag.MOD),self.words)
        reserve(Word("and",Tag.AND),self.words)
        reserve(Word("or",Tag.OR),self.words)

        self.file = InputFile(filename)
        self.peek = ''

        pass

    def getReserved(self,key):
        if key in self.words:
            return self.words[key]

    def readCh(self):

        self.peek = self.file.getChar()

    def checkReadChar(self, c):
        self.readCh()

        if self.peek != c:
            self.file.position += 1
            return False
        self.file.position += 1
        return True

    def emSpaces(self):
        self.peek = self.file.peekCh()
        while self.peek.isspace():
            self.readCh()


    def readCharString(self):
        auxString = "" + self.peek
        self.peek = self.file.getChar()
        while self.peek != '"' :
            auxString += self.peek
            self.peek = self.file.getChar()
        auxString += self.peek
        self.readCh()

        return CharacterString(auxString)

    def readComments(self):
        prev = self.file.position
        curr = self.file.position + 1

        while curr < self.file.size and self.file.data[prev] != "*" and self.file.data[curr] != ")":
            prev = curr
            curr += 1

        self.file.position = curr + 1
        return Token(Tag.COMMENTS)

    def scan(self):
        self.emSpaces()




        if self.peek == "(":
            if self.checkReadChar("*"):
                return self.readComments()

            else:
                return Token("(")

        elif self.peek == "<":
            if self.checkReadChar("="):
                return self.getReserved("<=")
            elif self.peek == ">":
                return self.getReserved("<>")
            else:
                return Token("<")

        elif self.peek == ">":
            if self.checkReadChar("="):
                return self.getReserved(">=")
            else:
                return Token(">")

        elif self.peek == "=":
            if self.checkReadChar("="):
                return self.getReserved("==")
            else:
                return Token("=")

        elif self.peek == ":":
            if self.checkReadChar("="):
                return self.getReserved(":=")
            else:
                return Token(":")

        elif self.peek == '"':
                return self.readCharString()

        if self.peek.isdigit():
            auxSD = ""
            auxSD += str(self.peek)
            self.readCh()
            while self.peek.isdigit():
                auxSD += str(self.peek)
                self.readCh()
            if self.peek != ".":
                return Integer(int(auxSD))

            auxSD += str(self.peek)
            while True:
                self.readCh()
                if self.peek.isdigit() == False:
                    break
                auxSD += str(self.peek)
            return Real(float(auxSD))






def wordprep(wordList, wds):

    for w in wordList:
        reserve(w,wds)

    pass

def reserve(w,wds):
    wds[w.lexeme] = w
