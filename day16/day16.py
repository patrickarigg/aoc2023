from utils.data import get_data
import numpy as np

def do_move(grid,mirrors,x_start,y_start,dir):
    new_moves = []
    if dir=='right':
        for j in range(y_start+1,grid.shape[1]):
            val = grid[x_start,j]
            if val == '.':
                grid[x_start,j]='#'
            if val== '-':
                mirrors.append((x_start,j))
            if val=='/':
                mirrors.append((x_start,j))
                new_moves.append((x_start,j,'up'))
                break
            if val=='\\':
                mirrors.append((x_start,j))
                new_moves.append((x_start,j,'down'))
                break
            if val=='|':
                mirrors.append((x_start,j))
                new_moves.append((x_start,j,'up'))
                new_moves.append((x_start,j,'down'))
                break

    if dir=='left':
        for j in range(y_start-1,-1,-1):
            val = grid[x_start,j]
            if val == '.':
                grid[x_start,j]='#'
            if val== '-':
                mirrors.append((x_start,j))
            if val=='/':
                mirrors.append((x_start,j))
                new_moves.append((x_start,j,'down'))
                break
            if val=='\\':
                mirrors.append((x_start,j))
                new_moves.append((x_start,j,'up'))
                break
            if val=='|':
                mirrors.append((x_start,j))
                new_moves.append((x_start,j,'up'))
                new_moves.append((x_start,j,'down'))
                break

    if dir=='up':
        for i in range(x_start-1,-1,-1):
            val = grid[i,y_start]
            if val == '.':
                grid[i,y_start]='#'
            if val== '-':
                mirrors.append((i,y_start))
                new_moves.append((i,y_start,'left'))
                new_moves.append((i,y_start,'right'))
                break
            if val=='/':
                mirrors.append((i,y_start))
                new_moves.append((i,y_start,'right'))
                break
            if val=='\\':
                mirrors.append((i,y_start))
                new_moves.append((i,y_start,'left'))
                break
            if val=='|':
                mirrors.append((i,y_start))

    if dir=='down':
        for i in range(x_start+1,grid.shape[0]):
            val = grid[i,y_start]
            if val == '.':
                grid[i,y_start]='#'
            if val== '-':
                mirrors.append((i,y_start))
                new_moves.append((i,y_start,'left'))
                new_moves.append((i,y_start,'right'))
                break
            if val=='/':
                mirrors.append((i,y_start))
                new_moves.append((i,y_start,'left'))
                break
            if val=='\\':
                mirrors.append((i,y_start))
                new_moves.append((i,y_start,'right'))
                break
            if val=='|':
                mirrors.append((i,y_start))
    # print(grid)
    return new_moves, mirrors


def part1(data):
    grid = np.array([[*row] for row in data])
    # print(grid)
    #beam comes in the top left initially
    all_moves = [(0,-1,'right')]
    moves = [(0,-1,'right')]
    mirrors = []

    while(len(moves)>0):
        # print(moves)
        x_start,y_start,dir = moves.pop(0)
        new_moves, mirrors_hit = do_move(grid,mirrors,x_start,y_start,dir)
        for move in new_moves:
            if move not in all_moves:
                moves.append(move)
                all_moves.append(move)
        for mirror in mirrors_hit:
            if mirror not in mirrors:
                mirrors.append(mirrors_hit)

    for mirror in mirrors:
        i,j = mirror
        grid[i,j]='#'

    return np.count_nonzero(grid=='#')

def part2(data):
    grid = np.array([[*row] for row in data])

    #generate possible start points
    start_points = []
    for i in range(grid.shape[0]):
        start_points.append((i,-1,'right'))
    for i in range(grid.shape[0]):
        start_points.append((i,grid.shape[1],'left'))
    for j in range(grid.shape[1]):
        start_points.append((-1,j,'down'))
    for j in range(grid.shape[1]):
        start_points.append((grid.shape[0],j,'up'))

    print(len(start_points))
    #beam comes in the top left initially
    results = []
    count=0
    for start_point in start_points:
        count+=1
        print('progress',count/len(start_points)*100,'%')
        gridcopy = np.ndarray.copy(grid)
        # print(gridcopy)

        all_moves = [start_point]
        moves = [start_point]
        mirrors = []

        while(len(moves)>0):
            # print(moves)
            x_start,y_start,dir = moves.pop(0)
            new_moves, mirrors_hit = do_move(gridcopy,mirrors,x_start,y_start,dir)
            for move in new_moves:
                if move not in all_moves:
                    moves.append(move)
                    all_moves.append(move)
            for mirror in mirrors_hit:
                if mirror not in mirrors:
                    mirrors.append(mirrors_hit)

        for mirror in mirrors:
            i,j = mirror
            gridcopy[i,j]='#'

        results.append(np.count_nonzero(gridcopy=='#'))
    return max(results)

if __name__=='__main__':
    data_dict =get_data(16)
    data = data_dict['data.txt']

    # result_part1 = part1(data)
    # print("part1:",result_part1)

    result_part2 = part2(data)
    print("part2:",result_part2)
