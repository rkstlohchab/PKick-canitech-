def minus_plus(n, k):
    original_n = n
    if n > 0:
        return minus_plus(n-k,k)
    else:
        if n != original_n:
            return minus_plus(n + k,k)
minus_plus(3,1)


# n, k = map(int, input().split())
# bill = 0 - k
# for i in range(n):
#     time, data = map(int, input().split())
#     bill += (data * time)
# print(bill)