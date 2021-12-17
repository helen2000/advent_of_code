import numpy as np
input = open("input.txt", "r")
map = []
def setup():
    map = []
    for each in input:
        line = each.split("\n")[0]
        temp_holder = list(line)
        for i in range(0, len(temp_holder)):
            temp_holder[i] = int(temp_holder[i])
        map.append(temp_holder)
    #import pdb; pdb.set_trace()
    return map

def low_point(pointx, pointy, max_x, max_y, map):
    '''
        check if current point is bigger than adjacent points
    '''
    current_point = map[pointy][pointx]
    if current_point == '*':
        return False
    if pointy > 0:
        if type(map[pointy-1][pointx]) == int and current_point>=map[pointy-1][pointx]:
            return False
    if pointy+1 < max_y:
        if type(map[pointy+1][pointx]) == int and current_point>=map[pointy+1][pointx]:
            return False
    if pointx > 0:
        if type(map[pointy][pointx-1]) == int and current_point>=map[pointy][pointx-1]:
            return False
    if pointx+1 < max_x:
        if type(map[pointy][pointx+1]) == int and current_point>=map[pointy][pointx+1]:
            return False
    return True



def find_risk_of_low(map, biggest_lowpoint):
    '''
    '''
    max_x = len(map[0])
    max_y = len(map)
    risk_count = 0
    for i in range(0, max_y):
        for k in range(max_x):
            if low_point(k, i, max_x, max_y, map):
                #import pdb; pdb.set_trace()
                if map[i][k] != 9:
                    print("low_point: ", map[i][k])
                    risk_count = risk_count + map[i][k] + 1
                    biggest_lowpoint = find_basin_size(k, i, max_x, max_y, map, biggest_lowpoint)
    return risk_count, biggest_lowpoint


def rec_basin_size(pointx, pointy, max_x, max_y, map, count):   
    '''
    '''
    #import pdb; pdb.set_trace()
    current_point_val = map[pointy][pointx]
    map[pointy][pointx] = "*"
    count+=1
    if current_point_val == '*':
        return count
    if pointy > 0:
        if type(map[pointy-1][pointx]) == int and map[pointy-1][pointx]<9:
            #import pdb; pdb.set_trace()
            count = rec_basin_size(pointx, pointy-1, max_x, max_y, map, count)
    if pointy+1 < max_y:
        #import pdb; pdb.set_trace()
        if type(map[pointy+1][pointx])==int and map[pointy+1][pointx]<9:
            #import pdb; pdb.set_trace()
            count = rec_basin_size(pointx, pointy+1, max_x, max_y, map, count)
    if pointx > 0:
        if type(map[pointy][pointx-1])==int and map[pointy][pointx-1] <9:
            
            count = rec_basin_size(pointx-1, pointy, max_x, max_y, map, count)
    if pointx+1 < max_x:
        if type(map[pointy][pointx+1])==int and map[pointy][pointx+1] <9:
           
            count = rec_basin_size(pointx+1, pointy, max_x, max_y, map, count)
    return count

def find_basin_size(pointx, pointy, max_x, max_y, map, biggest_lowpoint):
    '''
    '''
    
    size = rec_basin_size(pointx, pointy, max_x, max_y, map, 0)
    print("size: ", size)
    index = np.where(biggest_lowpoint == np.amin(biggest_lowpoint))
    pos = index[0][0]
    if biggest_lowpoint[pos]<size:
        biggest_lowpoint[pos] = size
    
    #import pdb; pdb.set_trace()
    return biggest_lowpoint
    #biggest_lowpoint
            


def print_map(map):
    for each in map:
        print(each)

biggest_lowpoint = np.array([0,0,0])
map = setup()
print_map(map)
risk, lowpoint_cal = find_risk_of_low(map, biggest_lowpoint)
print("q1 low risk ", risk)
print("q2 lowpoint size: ", lowpoint_cal, " product: ", np.prod(lowpoint_cal))
