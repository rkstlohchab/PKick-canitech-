lower = 1
upper = 100


for num in range(lower, upper + 1):
    # new_num = num//2
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

# my_list = [11, 12, 13, 15,16 ,17, 21]
# for numbers in my_list:
#     if numbers % 5 == 0:
#         print("this is divisble by 5 ")
#         break
# else:
#     print("NO number is divisible by 5 ")