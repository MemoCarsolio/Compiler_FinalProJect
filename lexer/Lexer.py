from .Word import *
from .Tag import *
from .InputFile import *



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

    def isReserved(self,key):
        if key in self.words:
            pass
    def readCh(self):
        self.peek = self.file.getChar()

    def emSpaces(self):
        self.peek = self.file.peekCh()
        while self.peek.isspace():
            self.peek + self.file.getChar()

    def readCharString(self):
        auxString = ""
        self.peek = self.file.getChar()
        while self.peek != '"' :
            auxString += self.peek

        auxString += self.peek
        readCh()

        return CharacterString(auxString)

    def readComments(self):
        prev = self.file.position
        curr = self.file.position + 1

        while current < self.file.size and self.file.data[prev] != "*" and self.file.data[curr] != ")":
            prev = curr
            curr += 1

        self.file.position = curr + 1
        return Token(Tag.COMMENTS)



def wordprep(wordList, wds):

    for w in wordList:
        reserve(w,wds)

    pass

def reserve(w,wds):
    wds[w.lexeme] = w
