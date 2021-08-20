directions = ["east", "south","north", "west", "east"]
original_i = 0
i_plus = 1
for i in range(len(directions)-1):
    if i_plus < 5:
        if directions[original_i] == 'east' and directions[i_plus] == 'west':
            directions.pop(original_i)
            directions.pop(i_plus)
        elif directions[original_i] == "north" and directions[i_plus] == 'south':
            directions.pop(original_i)
            directions.pop(i_plus)
        elif directions[original_i] == 'west' and directions[i_plus] == 'east':
            directions.pop(original_i)
            directions.pop(i_plus)
        elif directions[original_i] == "south" and directions[i_plus] == 'north':
            directions.pop(original_i)
            directions.pop(i_plus)
        original_i += 1
        i_plus += 1

print(new_direc)