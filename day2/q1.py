input = open("input.txt", "r")
hor_pos = 0
dep_pos = 0

for line in input:
    
    command = line.split(" ")[0]
    if command == "forward":
        hor_pos += int((line.split(" ")[1]).split("\n")[0])
    elif command == "up":
        dep_pos -= int((line.split(" ")[1]).split("\n")[0])
    else:
        dep_pos += int((line.split(" ")[1]).split("\n")[0])

print("depth: ", dep_pos, " - horizontal: ", hor_pos, " - muiltiplied: ", dep_pos*hor_pos)