a = int(input())
b = int(input())
c = int(input())

if a < b:
    if b < c:
        largest = c
        small = a
        small_a = b
    else:
        largest = b
        small = a
        small_a = c
else:
    if a > c:
        largest = a
        small = b
        small_a = c
    else:
        largest = c
        small = a
        small_a = b

if (small**2 + small_a**2) == largest**2:
    print("this is triplet")
else:
    print("Try other triplet")
