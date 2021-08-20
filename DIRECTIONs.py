directions = ["east", "south","north", "west", "east"]
new_direc = []
index = 0
for i in directions[:-1]:
    if i == "east" and directions[index + 1] != "west":
        if i == "east" and directions[index - 1] != "west":
            new_direc.append(i)
    elif i == "north" and directions[index + 1] != "south":
        if i == "north" and directions[index-1] != "south":
            new_direc.append(i)
    elif i == "west" and directions[index + 1] != "east":
        if i == "west" and directions[index - 1] != "east":
            new_direc.append(i)
    elif i == "south" and directions[index + 1] != "north":
        if i == "south" and directions[index-1] != "north":
            new_direc.append(i)
    index += 1
print(new_direc)