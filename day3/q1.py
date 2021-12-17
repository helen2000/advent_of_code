input = open("input.txt", "r")
ep_count = [0] *12
count = 0

# count is array of count for each column
for line in input:
    binary = line.split("\n")[0]
    for i in range(0, len(binary)):
        ep_count[i] += int(binary[i])
    count +=1

# build binary array 
ep = []
ga = []
for value in ep_count:
    if value > count/2:
        ep.append("1")
        ga.append("0")
    else: 
        ep.append("0")
        ga.append("1")

ep = "".join(ep)
ga = "".join(ga)
ep_dec = 0
ga_dec = 0
# convert binary to decimal
if ep[len(ep)-1] == "1":
    ep_dec += 1
else:
    ga_dec += 1

for i in range(len(ep)-2, -1, -1):
    if ep[i] == "1":
        ep_dec += 2**(len(ep)-1-i)
    else:
        ga_dec += 2**(len(ep)-1-i)

print("power consumption: ", ep_dec * ga_dec)