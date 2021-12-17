import numpy as np
import math
input = open("input.txt", "r")
chunk_pairs = {
    '(': ')',
    '{': '}',
    '<': '>',
    '[': ']',
}
error_to_point = {
    ')': 3,
    '}': 1197,
    '>': 25137,
    ']': 57,
}
autocomplete_to_point = {
    ')': 1,
    '}': 3,
    '>': 4,
    ']': 2,
}
subsystem = []
def setup():
    system = []
    for each in input:
        line = each.split("\n")[0]
        temp_holder = list(line)
        system.append(temp_holder)
    #import pdb; pdb.set_trace()
    return system

def run_sim(subsystem):
    keys = chunk_pairs.keys()
    arr_of_fail = []
    completion_values = []
    for line in subsystem:
        open_arr = []
        stop = False
        for val in line:
            if val in keys:
                open_arr.append(val)
            else:
                #must be a close bracket
                if len(open_arr)<1:
                    #only close bracket in row
                    arr_of_fail.append(val)
                    stop = True
                elif chunk_pairs.get(open_arr[-1]) == val:
                    #success
                    open_arr.pop()
                else:
                    arr_of_fail.append(val)
                    stop = True
            if stop:
                break
        if len(open_arr)>0 and not stop:
            # line is incomplete
            c_val = cal_completion(open_arr)
            completion_values.append(c_val)
    return arr_of_fail, completion_values

def cal_completion(arr):
    count=0
    for i in range(len(arr)-1, -1, -1):
        count *= 5
        count += autocomplete_to_point.get(chunk_pairs.get(arr[i]))
    print(arr," : ", count)
    return count

def calculate_error(arr_of_fail):
    count = 0
    for val in arr_of_fail:
        count += error_to_point.get(val)
    return count

subsystem = setup()
arr_of_fail, completion_val = run_sim(subsystem)
print("error value is: ", calculate_error(arr_of_fail))
print("completion value is: ", np.sort(np.array(completion_val))[math.floor(len(completion_val)/2)])
