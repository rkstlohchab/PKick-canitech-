# my_string = '123'
# my_list = [int(element) for element in my_string]
# length = len(my_string)
# product = 1
# while (length > 1):
#     product *= element
#     product = my_string
# print(new_digit)

# b = int(input("Side of triangle:"))
# p = b
# s = int(input("side of square"))
# area_tri = 0.5 * b * p
# area_square = s * s
# print("total number of square that can fit in triangle are {}".format(area_tri//area_square))

x = 24
y = 30

for i in range(1, y + 1):
    if((x % i == 0) and (y % i == 0)):
        hcf = i
print(hcf)