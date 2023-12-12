from utils.data import get_data
import numpy as np

def get_expanded_universe(data):
    universe = [list(row) for row in data]
    universe = np.array(universe)
    n_rows = universe.shape[0]
    n_cols = universe.shape[1]
    empty_rows = []
    empty_cols = []

    for i in range(n_rows):
        if np.array_equal(universe[i,:],["."]*n_cols):
            empty_rows.append(i)

    for j in range(n_cols):
        if np.array_equal(universe[:,j],["."]*n_rows):
            empty_cols.append(j)

    empty_rows = np.array(empty_rows)
    empty_cols = np.array(empty_cols)
    print(empty_rows,empty_cols)

    universe = np.insert(universe,empty_rows,".",axis=0)
    universe = np.insert(universe,empty_cols,".",axis=1)

    return universe

def calculate_distance(galaxy1,galaxy2):
    return abs(galaxy1[0]-galaxy2[0])+abs(galaxy1[1]-galaxy2[1])

def calculate_distance_2(galaxy1,galaxy2,universe,expansion):
    #galaxies between rows
    r1 = galaxy1[0]
    r2 = galaxy2[0]
    c1 = galaxy1[1]
    c2 = galaxy2[1]
    empty_rows = 0
    empty_cols = 0

    for i in range(*sorted([r1,r2])):
        if np.array_equal(universe[i,:],["."]*universe.shape[1]):
            empty_rows+=1

    for j in range(*sorted([c1,c2])):
        if np.array_equal(universe[:,j],["."]*universe.shape[0]):
            empty_cols+=1

    return abs(r1-r2)+abs(c1-c2)+(empty_rows+empty_cols)*(expansion-1)

    #galaxies between cols

def part1(data):

    # expand universe by finding empty rows and cols
    universe = get_expanded_universe(data)
    # print(universe)

    # find galaxies
    galaxies = []

    for i in range(universe.shape[0]):
        for j in range(universe.shape[1]):
            if universe[i,j]=="#":
                galaxies.append((i,j))

    print(galaxies)

    # calculate distances
    all_dists = []
    combinations = []
    for g1 in galaxies:
        for g2 in galaxies:
            if sorted([g1,g2]) not in combinations:
                combinations.append(sorted([g1,g2]))
                dist = calculate_distance(g1,g2)
                all_dists.append(dist)

    print(all_dists)

    return sum(all_dists)

def part2(data,expansion=1):

    universe = [list(row) for row in data]

    # find galaxies
    universe = np.array(universe)

    galaxies = []
    for i in range(universe.shape[0]):
        for j in range(universe.shape[1]):
            if universe[i,j]=="#":
                galaxies.append((i,j))

    print(galaxies)

    # calculate distances
    all_dists = []
    combinations = []
    for g1 in galaxies:
        for g2 in galaxies:
            if (sorted([g1,g2]) not in combinations) and g1!=g2:
                combinations.append(sorted([g1,g2]))
                dist = calculate_distance_2(g1,g2,universe,expansion)
                all_dists.append(dist)

    print(all_dists)

    return sum(all_dists)

if __name__=='__main__':
    data_dict =get_data(11)
    data = data_dict['data.txt']

    # result_part1 = part1(data,1_000_000)
    # print("part1:",result_part1)

    result_part2 = part2(data,1_000_000)
    print("part2:",result_part2)
