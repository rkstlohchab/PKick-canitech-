n = int(input())
for i in range(n):
    household = int(input())
    x = int(input())
    y = int(input())
    total_w = int(input())
    if (x+y//2)*household <= total_w:
        print("YES")
    else:
        print("NO")