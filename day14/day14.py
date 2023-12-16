from utils.data import get_data
import numpy as np
import re

def move_up(dish_map,x,y):
    for i in range(x,0,-1):
        #swap if there is a '.'
        if dish_map[i-1,y]=='.':
            dish_map[i-1,y],dish_map[i,y] = dish_map[i,y], dish_map[i-1,y]
        else:
            break

def move_down(dish_map,x,y):
    for i in range(x,dish_map.shape[0]-1):
        #swap if there is a '.'
        if dish_map[i+1,y]=='.':
            dish_map[i+1,y],dish_map[i,y] = dish_map[i,y], dish_map[i+1,y]
        else:
            break

def move_left(dish_map,x,y):
    for j in range(y,0,-1):
        #swap if there is a '.'
        if dish_map[x,j-1]=='.':
            dish_map[x,j-1],dish_map[x,j] = dish_map[x,j], dish_map[x,j-1]
        else:
            break

def move_right(dish_map,x,y):
    for j in range(y,dish_map.shape[1]-1):
        #swap if there is a '.'
        if dish_map[x,j+1]=='.':
            dish_map[x,j+1],dish_map[x,j] = dish_map[x,j], dish_map[x,j+1]
        else:
            break

def perform_one_full_spin(dish_map):
    #check by going down cols
    for j in range(dish_map.shape[1]):
        for i in range(dish_map.shape[0]):
            if dish_map[i,j]=='.':
                continue
            if dish_map[i,j]=='O':
                #move up until i==0 or hit another rock or square rock
                move_up(dish_map,i,j)

    #check by going down the rows
    for i in range(dish_map.shape[0]):
        for j in range(dish_map.shape[1]):
            if dish_map[i,j]=='.':
                continue
            if dish_map[i,j]=='O':
                #move up until i==0 or hit another rock or square rock
                move_left(dish_map,i,j)

    #check by going up the cols
    for j in range(dish_map.shape[1]):
        for i in range(dish_map.shape[0]-1,-1,-1):
            if dish_map[i,j]=='.':
                continue
            if dish_map[i,j]=='O':
                #move up until i==0 or hit another rock or square rock
                move_down(dish_map,i,j)

    #check by going up the rows
    for i in range(dish_map.shape[0]):
        for j in range(dish_map.shape[1]-1,-1,-1):
            if dish_map[i,j]=='.':
                continue
            if dish_map[i,j]=='O':
                #move up until i==0 or hit another rock or square rock
                move_right(dish_map,i,j)

def part1(data):
    dish_map = np.array([[*line] for line in data])
    print(dish_map)
    #check by going down cols
    for j in range(dish_map.shape[1]):
        for i in range(dish_map.shape[0]):
            if dish_map[i,j]=='.':
                continue
            if dish_map[i,j]=='O':
                #move up until i==0 or hit another rock or square rock
                move_up(dish_map,i,j)
    print()
    print(dish_map)
    print()
    total = 0
    for i in range(dish_map.shape[0]):
        total+=sum(dish_map[i,:]=='O')*(dish_map.shape[0]-i)

    return total

def part2(data):
    dish_map = np.array([[*line] for line in data])
    print(dish_map)

    spin_results = []
    matches = []
    cycle = None
    offset = None
    for i in range(1_000_000_000):
        perform_one_full_spin(dish_map)
        total = 0
        for i in range(dish_map.shape[0]):
            total+=sum(dish_map[i,:]=='O')*(dish_map.shape[0]-i)

        spin_results.append(total)
        # print(' '.join(list(map(str,spin_results))))
        match = re.search(r"(.+ .+)( \1)+", ' '.join(list(map(str,spin_results))))
        if match:
            print(match.group(1))
            nums = [int(x) for x in match.group(1).split(' ') if x!='']
            matches.append(nums)
            if len(matches)>2 and 2*matches[-2]==matches[-1]:
                cycle = matches[-2]
                print(cycle)
                break

    for i in range(len(spin_results)):
        if spin_results[i:i+len(cycle)]==cycle:
            offset=i+1

    return cycle[((1_000_000_000 - offset) % len(cycle))]

if __name__=='__main__':
    data_dict =get_data(14)
    data = data_dict['test_data.txt']

    # result_part1 = part1(data)
    # print("part1:",result_part1)

    result_part2 = part2(data)
    print("part2:",result_part2)
