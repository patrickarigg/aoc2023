from utils.data import get_data

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.

#Valid next chars:
up_S = '|7F'
down_S = '|LJ'
left_S = '-LF'
right_S = '-7J'

up_VPipe = '|7F'
down_VPipe = '|LJ'
left_VPipe = ''
right_VPipe = ''

up_HPipe = ''
down_HPipe = ''
left_HPipe = '-LF'
right_HPipe = '-J7'

up_L = '|7F'
down_L = ''
left_L = ''
right_L = '-7J'

up_J = '|7F'
down_J = ''
left_J = '-FL'
right_J = ''

up_7 = ''
down_7 = '|LJ'
left_7 = '-FL'
right_7 = ''

up_F = ''
down_F = '|LJ'
left_F = ''
right_F = '-7J'

dir_dict = {
    'up':{'S':up_S, '|':up_VPipe, '-':up_HPipe,'L':up_L,'J':up_J,'7':up_7,'F':up_F},
    'down':{'S':down_S, '|':down_VPipe, '-':down_HPipe,'L':down_L,'J':down_J,'7':down_7,'F':down_F},
    'left':{'S':left_S, '|':left_VPipe, '-':left_HPipe,'L':left_L,'J':left_J,'7':left_7,'F':left_F},
    'right':{'S':right_S, '|':right_VPipe, '-':right_HPipe,'L':right_L,'J':right_J,'7':right_7,'F':right_F}
}

def get_next_pipe_piece_loc(data,curr_loc,pipe_map):
    i,j = curr_loc
    curr_char = data[i][j]
    surrounding_locations = [(i-1, j),(i+1, j),(i,j-1),(i, j+1)]
    next_pipe_piece_loc = None
    dirs = ['up','down','left','right']
    for dir, loc in zip(dirs,surrounding_locations):
        char = data[loc[0]][loc[1]]
        if (char in dir_dict[dir][curr_char]) and (loc not in pipe_map):
            next_pipe_piece_loc=loc
            break

    return next_pipe_piece_loc

def is_inside_loop(x,y,pipe_map,data):
    #always go right for ray cast
    intersect_count = 0
    perim_tracker = ''
    for j in range(y,len(data[0])):
        if ((x,j) in pipe_map) and data[x][j]=='|':
            intersect_count+=1
        if ((x,j) in pipe_map) and data[x][j] in 'L7FJ':
            perim_tracker += data[x][j]
    intersect_count+=perim_tracker.count('L7')+perim_tracker.count('FJ')
    if intersect_count%2!=0:
        return True
    return False

def part1(raw_data):
    #pad the data
    data = ['.'+raw_data[i]+'.' for i in range(len(raw_data))]
    data.insert(0,'.'*len(data[0]))
    data.append('.'*len(data[0]))

    #create distance grid to track max distance
    n_rows = len(data)
    n_cols = len(data[0])
    dist_grid = []
    for i in range(n_rows):
        dist_grid.append(['.']*n_cols)

    #find start point
    start_point = (0,0)
    for i in range(n_rows):
        for j in range(n_cols):
            if data[i][j]=='S':
                start_point = (i,j)
                dist_grid[i][j]=0

    pipe_map = [start_point]
    #find next part of pipe loop until back at 'S'
    count=0
    curr_loc = start_point
    while(True):
        next_loc = get_next_pipe_piece_loc(data,curr_loc,pipe_map)
        if next_loc:
            count+=1
            i,j = next_loc
            pipe_map.append(next_loc)
            dist_grid[i][j]=count
            curr_loc = next_loc
        else:
            break

    #find the furthest point
    mid_point = (count+1)//2
    return mid_point

def part2(raw_data):
    #ray casting - odd number of intersections for
    #pad the data
    data = ['.'+raw_data[i]+'.' for i in range(len(raw_data))]
    data.insert(0,'.'*len(data[0]))
    data.append('.'*len(data[0]))

    #create distance grid to track max distance
    n_rows = len(data)
    n_cols = len(data[0])
    dist_grid = []
    for i in range(n_rows):
        dist_grid.append(['.']*n_cols)

    #find start point
    start_point = (0,0)
    for i in range(n_rows):
        for j in range(n_cols):
            if data[i][j]=='S':
                start_point = (i,j)
                dist_grid[i][j]=0

    pipe_map = [start_point]
    #find next part of pipe loop until back at 'S'
    count=0
    curr_loc = start_point
    while(True):
        next_loc = get_next_pipe_piece_loc(data,curr_loc,pipe_map)
        if next_loc:
            count+=1
            i,j = next_loc
            pipe_map.append(next_loc)
            dist_grid[i][j]=count
            curr_loc = next_loc
        else:
            break

    enclosed_tiles_count = 0
    for i in range(n_rows):
        for j in range(n_cols):
            if (i,j) not in pipe_map and is_inside_loop(i,j,pipe_map,data):
                dist_grid[i][j]='I'
                enclosed_tiles_count+=1

    return enclosed_tiles_count

if __name__=='__main__':
    data_dict =get_data(10)
    data = data_dict['data.txt']

    result_part1 = part1(data)
    print("part1:",result_part1)

    result_part2 = part2(data)
    print("part2:",result_part2)
