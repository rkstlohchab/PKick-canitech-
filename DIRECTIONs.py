directions = ["east", "south","north", "west", "east"]
new_direc = []
original_i = 0
i_plus = 1

for i in range(len(directions)):
    if directions[original_i] == 'east' and directions[i_plus] != 'west':
        new_direc.append(directions[original_i])
        new_direc.append(directions[i_plus])
    if directions[original_i] == "north" and directions[i_plus] != 'south':
        new_direc.append(directions[original_i])
        new_direc.append(directions[i_plus])
    if directions[original_i] == 'west' and directions[i_plus] != 'east':
        new_direc.append(directions[original_i])
        new_direc.append(directions[i_plus])
    if directions[original_i] == "south" and directions[i_plus] != 'north':
        new_direc.append(directions[original_i])
        new_direc.append(directions[i_plus])
    original_i += 1
    i_plus += 1

print(new_direc)