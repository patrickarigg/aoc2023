from utils.data import get_data
import re
import math
import numpy as np

def part1(data):
    pattern = data[0]
    move_data = data[1:-1]

    #build  dicts
    R_dict = {}
    L_dict = {}
    for line in move_data:
        key,left,right = re.findall(r"(\w{3}) = \((\w{3}), (\w{3})\)",line)[0]
        L_dict[key] = left
        R_dict[key] = right

    # print(R_dict)
    # print(L_dict)

    count=0
    n = len(pattern)
    loc =  "AAA"
    while(True):
        next_dir = pattern[count%n]
        if next_dir=='L':
            loc = L_dict[loc]
        if next_dir=='R':
            loc = R_dict[loc]
        count+=1
        if loc=='ZZZ':
            break

    return count

def part2(data):
    pattern = data[0]
    move_data = data[1:-1]

    #build  dicts
    R_dict = {}
    L_dict = {}
    for line in move_data:
        key,left,right = re.findall(r"(\w{3}) = \((\w{3}), (\w{3})\)",line)[0]
        L_dict[key] = left
        R_dict[key] = right

    #fin all starting points
    starting_points = []
    for key in L_dict.keys():
        if key[-1]=='A':
            starting_points.append(key)

    n = len(pattern)
    steps_to_z = []
    for start in starting_points:
        steps = 0
        loc = start
        while loc[-1] != 'Z':
            next_dir = pattern[steps%n]
            if next_dir=='L':
                loc = L_dict[loc]
                steps+=1
            if next_dir=='R':
                loc = R_dict[loc]
                steps+=1
        steps_to_z.append(steps)

    return np.lcm.reduce(steps_to_z)

if __name__=='__main__':
    data_dict =get_data(8)
    data = data_dict['data.txt']

    result_part1 = part1(data)
    print("part1:",result_part1)

    result_part2 = part2(data)
    print("part2:",result_part2)
