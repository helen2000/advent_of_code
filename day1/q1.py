input = open("input.txt", "r")
prevline = None
inc_count = 0

for line in input:
    
    if prevline != None and int(line.split("\n")[0]) > prevline:
        inc_count +=1
    prevline = int(line.split("\n")[0])

print(inc_count)