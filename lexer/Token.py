


class Token:
    def __init__(self, tag):
        self.tag = tag

    def getTag(self):
        return self.tag

    def toString(self):
        return "TOKEN - VALUE = " + str(self.tag)
