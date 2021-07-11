a_string = 'aaaaaaaaaabcdefgh'
length = len(a_string)
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in a_string:
    for j in alpha:
        if i == j:
            n_s = i, i.count(i)
            a_s = str(i, sum(i.count(i))
