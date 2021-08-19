# my_l_a = []
# for i in range(int(input())):
#     num = int(input("Enter the numbers:"))
#     my_l_a.append(num)
#
# prod_list = []
#
# for j in range(len(my_l_a)):
#     for k in range(j + 1, len(my_l_a)):
#         a_num = my_l_a[j] * my_l_a[k]
#         prod_list.append(a_num)
#
# maxi = max(prod_list)
# sum = 0
#
# for l in str(maxi):
#     sum += int(l)
#
# print(sum)

class MyListA():
    my_l_a = []
    prod_list = []
    def __init__(self, i_range):
        self.i_range = i_range
    def iterator(self):
        for i in range(self.i_range):
            num = int(input("Enter the numbers:"))
            my_l_a.append(num)
    def prod_iterator(self):
        for j in range(len(my_l_a)):
            for k in range(j + 1, len(my_l_a)):
                a_num = my_l_a[j] * my_l_a[k]
                prod_list.append(a_num)
    def max_prod(self):
        maxi = max(prod_list)
        sum = 0

        for l in str(maxi):
            sum += int(l)

        print(sum)


range = MyListA(i_range=1)
range.iterator()
range.prod_iterator()
range.max_prod()