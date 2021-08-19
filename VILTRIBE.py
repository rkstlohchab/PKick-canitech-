village = 'A..A..B...B'
splitted_village = [char for char in village]

flag_a = 0
flag_b = 0
dot = 0
count_a = 0
count_b = 0
for i in village:
    if i == 'A' and flag_a == 0:
        flag_a = 1
        count_a += 1
        flag_b = 0
        count_b = 0
    elif i == 'A' and flag_a ==1:
        flag_a += 1
    elif i == 'B' and flag_b == 1:
        flag_b += 1
    elif i == '.' and flag_a == 1:
        dot += 1
        count_a += 1
    elif i == 'B' and flag_b == 0:
        flag_b = 1
        count_b += 1
        flag_a = 0
        count_a = 0
    elif i == '.' and flag_b == 1:
        dot += 1
        count_b += 1
print(count_a)
print(count_b)