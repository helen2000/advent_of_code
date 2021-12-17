input = open("input.txt", "r")
col_count = [0] *12

input = [
    line.split("\n")[0] for line in input
]

# count is array of count for each column
def getMostCommon(ins, pos):
    count = 0
    pos_count = 0
    for binary in ins:
        pos_count += int(binary[pos])
        count +=1

    if pos_count>= count/2:
        return "1"
    else:
        return "0"

num_len = len(input[0])
ox_gen = input
co2_scrub = input
tempo =[]
tempc = []
for i in range(0, num_len):
    if len(ox_gen) <=1:
        break
    most_common = getMostCommon(ox_gen, i)
    for ox in ox_gen:
        if ox[i] == most_common:
            tempo.append(ox) 
    ox_gen = tempo
    tempo = []

for i in range(0, num_len):
    if len(co2_scrub) <=1:
        break
    most_common = getMostCommon(co2_scrub, i)
    for co in co2_scrub:
        if co[i] != most_common:
            tempc.append(co)
    co2_scrub = tempc
    tempc = []
 
ox_gen = ox_gen[0]
co2_scrub = co2_scrub[0]

ox_num = 0
co2_num = 0

# convert binary to decimal
if ox_gen[len(ox_gen)-1] == "1":
    ox_num += 1
if co2_scrub[len(co2_scrub)-1] == "1":
    co2_num += 1

for i in range(len(ox_gen)-2, -1, -1):
    if ox_gen[i] == "1":
        ox_num += 2**(len(ox_gen)-1-i)
    if co2_scrub[i] == "1":
        co2_num += 2**(len(ox_gen)-1-i)

print("life support rating: ", ox_num * co2_num)
import pdb; pdb.set_trace()

