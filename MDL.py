nums = list(map(int, input().split()))
while len(nums) != 2:
    sliced_num = nums[:3]
    sliced_num.sort()
    nums.remove(sliced_num[1])

print(nums)