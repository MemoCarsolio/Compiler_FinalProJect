from lexer_f import *
import pandas as pd
import math
from .grammar import *


class Parser:
    def __init__(self, input):

        self.input_t = parser_prep(input)
        self.stack = []
        self.stack.append(0)
        self.table = pd.read_csv(
            "parser_f/Grammar.csv", header=[0], index_col=[0])
        self.next = self.table[self.input_t[0]['token']][self.stack[0]]
        self.prevR = self.stack[0]

    def parse(self):

        if not (isinstance(self.next, float) or isinstance(self.next, int)):

            if str(self.next[0]) == "s":
                self.shift()
            elif str(self.next[0]) == "r":
                self.reduce()

            elif self.next == "acc":
                print("Succesfull Compilation | Exit Code (0)")
                exit()
            else:
                print('Warning: Unexpected Error: 4096')

        elif math.isnan(self.next):
            if self.input_t[0]["token"] == "$":
                print(
                    "E0F Error: '" + self.prevR["value"] + "' pos[" + str(self.prevR["line"]) + ", " + str(
                        self.prevR["col"]) + "] : ")
            else:
                print(
                    "Syntax Error: '" + self.prevR["value"] + "'  pos[" + str(self.prevR["line"]) + ", " + str(
                        self.prevR["col"]) + "] ")
            print("Compilation aborted")
        else:
            self.prevR = self.input_t[0]
            self.stack.append(int(self.next))
            self.next = self.table[self.input_t[0]["token"]][self.stack[-1]]

            self.parse()

    def shift(self):

        self.stack.append(self.input_t[0]["token"])
        self.stack.append(int(self.next[1:len(self.next)]))
        self.prevR = self.input_t[0]
        self.input_t.pop(0)
        self.next = self.table[self.input_t[0]
                               ["token"]][self.stack[-1]]
        self.parse()

    def reduce(self):
        value = grammar[int(self.next[1:len(self.next)])]["value"]
        remove = grammar[int(
            self.next[1:len(self.next)])]["remove"]
        self.prevR = self.input_t[0]
        if remove == 0:
            self.stack.append(value)
            self.next = self.table[self.stack[-1]][self.stack[-2]]
            self.parse()
        else:

            self.stack = self.stack[:len(self.stack) - remove]
            self.stack.append(value)
            self.next = self.table[self.stack[-1]][self.stack[-2]]
            self.parse()


def parser_prep(input):
    lex = Lexer(input)
    tokens_dl = []
    while True:
        aux = lex.scan()
        line = lex.getLine()
        col = lex.getColumn()

        if aux.getTag() == 65535:
            break
        if aux.getTag() != 292:
            if hasattr(aux, 'value'):
                tokens_dl.append({'token': aux.toString(), 'line': line,
                                  'col': col, 'value': aux.getValue()})
            elif aux.getTag() == 290:
                tokens_dl.append({'token': 'id', 'line': line,
                                  'col': col, 'value': aux.toString()})
            else:
                tokens_dl.append({'token': aux.toString(), 'line': line,
                                  'col': col, 'value': aux.toString()})

    tokens_dl.append(
        {"token": "$", "line": tokens_dl[-1]["line"], "col": tokens_dl[-1]["col"], "value": "EOF"})
    return tokens_dl
