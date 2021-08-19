class Pair():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def check_pair(self):
        if self.a == self.b or self.b == self.c or self.a == self.c:
            print("YES")
        else:
            print("NO")
pair = Pair(a="white", b="white", c="black")
pair.check_pair()