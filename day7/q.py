import numpy as np
import math
input = open("input.txt", "r")
crabs = []

def setup():
    for each in input:
        line = each.split("\n")[0]
        crabs = line.split(",")
        for i in range(0, len(crabs)):
            crabs[i] = int(crabs[i])
    #pdb; pdb.set_trace()
    return crabs

def calculate_fuel_one(crabs):
    pos_to_move_to = np.median(crabs)
    dis_arr = np.bincount(crabs)
    fuel = 0
    for i in range(0, len(dis_arr)):
        fuel += dis_arr[i] * np.sqrt(pow(pos_to_move_to-i, 2))
    return fuel, pos_to_move_to

def calculate_fuel_two(crabs):
    pos_to_move_to = math.floor(np.mean(crabs))
    dis_arr = np.bincount(crabs)
    fuel = 0
    for i in range(0, len(dis_arr)):
        movement = int(np.sqrt(pow(pos_to_move_to-i, 2)))
        fuel += dis_arr[i] * ((movement*(movement+1))/2)
    return fuel, pos_to_move_to

crabs = setup()
fuel, pos = calculate_fuel_one(crabs)
print("q1 crabs should move to ", pos, " taking up ", fuel, " units of fuel")
fuel, pos = calculate_fuel_two(crabs)
print("q2 crabs should move to ", pos, " taking up ", fuel, " units of fuel")

