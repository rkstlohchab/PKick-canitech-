work_l = []


for i in range(int(input())):
    work = int(input())
    work_l.append(work)

#counts the number of ones
count = 0
#for selecting one of the output
check_life = 0

#iterates over our list to check if there is 5 "1" together or not
for j in work_l:
    if j == 1:
        count += 1
    elif j == 0:
        count = 0
    if count > 5:
        check_life = 1
        break

#checks and prints if the coder is bored or not
if check_life == 1:
    print('#coderlifematters')
else:
    print('#allcodersarefun')
