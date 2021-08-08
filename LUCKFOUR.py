class LuckFour():
    def __init__(self, luck_four):
        self.luck_four = luck_four
    def luck_list(self):
        luck_list = []
        for i in self.luck_four:
            luck_list.append(i)
        four = luck_list.count('4')
        print(four)
luck = input()
my_num = LuckFour(luck)
my_num.luck_list()
