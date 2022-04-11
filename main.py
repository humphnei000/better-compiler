class Stream:
    def __init__(self,data):
        self.data = list(data)
        self.inx = 0
    def at(self,i=0):
        return self.data[self.inx + i]
    def inc(self,i=1):
        self.inx += i

class ExpStatement:
    def __init__(self,exp):
        self.exp = exp
def readStatement(strm):
    pass

with open("src.txt") as file:
    data = file.read()
    print(data)
    strm = Stream(data)