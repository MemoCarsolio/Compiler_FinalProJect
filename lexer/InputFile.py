class InputFile:

    def __init__(self, filename):
        self.file = open(filename, "r")
        self.data = []
        self.position = 0
        self.lineN = 1
        self.columnN = 1
        aux = self.file.read()
        self.lines = 0
        self.size = 0
        for ch in aux:
            self.size += 1
            if ch == "\n":
                self.lines += 1
            self.data.append(ch)

    def getChar(self):
        self.position += 1

        c = self.data[self.position]
        if c == "\n":
            self.columnN = 1
            self.lineN += 1
        else:
            self.columnN += 1

        return c

    def peekCh(self):
        return self.data[position]


    def isE0F(self):
        if self.lineN == self.lines:
            return True
        else:
            return False
