import numpy as np
input = open("input.txt", "r")
lanten_fish = []

def setup():
    for each in input:
        line = each.split("\n")[0]
        lanten_fish = line.split(",")
        for i in range(0, len(lanten_fish)):
            lanten_fish[i] = int(lanten_fish[i])
    #pdb; pdb.set_trace()
    return lanten_fish

def run_sim(num_of_days, lanten_fish):
    for day in range(0, num_of_days):
        for i in range(0, len(lanten_fish)):
            if lanten_fish[i] == 0:
                lanten_fish[i] = 6
                lanten_fish.append(8)
            else:
                lanten_fish[i] -=1
        #print("day ", day, " there are ", len(lanten_fish), " many fish.")
    return len(lanten_fish)

lanten_fish = setup()
lantan_arr = np.array(lanten_fish)
count = 0
def operation_func(element):
    if element >0:
        return element -1
    else:
        return 6

def run_sim_numpy(num_of_days, lantan_arr):
    '''
        sim run with numpy for speed
    '''
    minus_one_vector = np.vectorize(operation_func)
    for day in range(0, num_of_days):
        #import pdb; pdb.set_trace()
        arr_of_new = np.full(np.bincount(lantan_arr)[0], 8)
        lantan_arr = minus_one_vector(lantan_arr)
        lantan_arr = np.append(lantan_arr, arr_of_new)
        print("day ", day, " there are ", len(lantan_arr), " many fish.")
    return len(lantan_arr)

def run_sim_approach_two(num_of_days, lantan_arr):
    '''
        run sim quicker
    '''
    dis_arr = np.append(np.bincount(lantan_arr), [0, 0,0])
    for day in range(0, num_of_days):
        dis_arr = np.roll(dis_arr, -1)
        dis_arr[5] = dis_arr[5] + dis_arr[7]
        #print("day ", day, " there are ", sum(dis_arr), " many fish.")
    return sum(dis_arr)


run_sim_approach_two(257, lantan_arr)
print("q1) number of lantern fish: ", run_sim(80, lanten_fish))
print("q2) number of lantern fish: ", run_sim_approach_two(257, lantan_arr))