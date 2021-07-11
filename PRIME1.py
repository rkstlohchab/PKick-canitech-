a = 1
b = 7

for i in range(a, b+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
