my_l_a = []
for i in range(int(input())):
    num = int(input("Enter the numbers:"))
    my_l_a.append(num)

prod_list = []

for j in range(len(my_l_a)):
    for k in range(j + 1, len(my_l_a)):
        a_num = my_l_a[j] * my_l_a[k]
        prod_list.append(a_num)

maxi = max(prod_list)
sum = 0

for l in str(maxi):
    sum += int(l)

print(sum)00