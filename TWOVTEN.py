ten = int(input())
for i in range(0,ten):
    x = int(input())
    if x % 10 == 0:
        print(0)
    elif x % 5==0:
        print(1)
    else:
        print(-1)
    print()
