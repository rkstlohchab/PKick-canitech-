class T20Match():
    def __init__(self,r,o,c):
        self.r = r
        self.o = o
        self.c = c
    def possibility(self):
        remaning_over = 20 - self.o
        can_score = remaning_over * 6 * 6
        victory_run = self.c + can_score
        if (victory_run > self.r):
            print("yes")
        else:
            print("no")
match = T20Match(r=719, o=18, c=648)
match.possibility()