input = open("input.txt", "r")
firstline = None
secondline = None
prevsum = None
inc_count = 0

for line in input:
    if secondline != None: 
        sum = firstline + secondline + int(line.split("\n")[0])
        if prevsum != None and sum>prevsum:
            inc_count +=1
        prevsum = sum
        firstline = secondline
        secondline = int(line.split("\n")[0])
    elif secondline == None:
        if firstline == None:
            firstline = int(line.split("\n")[0])
        else:
            secondline = int(line.split("\n")[0])
        

print(inc_count)