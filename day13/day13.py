from utils.data import get_data
import numpy as np

def check_rows(pattern):
    # print('checking rows')
    for i in range(1,pattern.shape[0]):
        l = min(i,pattern.shape[0]-i)
        # print("l:",l)
        sub_pattern_1 = pattern[i-l:i]
        sub_pattern_2 = pattern[i:i+l]
        # print(sub_pattern_1)
        # print(np.flipud(sub_pattern_2))
        if np.array_equal(sub_pattern_1,np.flipud(sub_pattern_2)):
            return i-1
    return None
def check_cols(pattern):
    # print('checking cols')
    for i in range(1,pattern.shape[1]):
        # print(pattern.shape[1])
        l = min(i,pattern.shape[1]-i)
        # print("l:",l)
        sub_pattern_1 = pattern[:,i-l:i]
        sub_pattern_2 = pattern[:,i:i+l]
        # print(sub_pattern_1)
        # print(np.fliplr(sub_pattern_2))
        if np.array_equal(sub_pattern_1,np.fliplr(sub_pattern_2)):
            return i-1
    return None
def part1(data):
    patterns_data = data.split('\n\n')
    patterns = [pattern_data.split('\n') for pattern_data in patterns_data]
    patterns[-1].remove('')
    patterns = [np.array([[*line] for line in pattern]) for pattern in patterns]

    row_results = []
    col_results = []
    for pattern in patterns:
        # print('pattern:')
        # print(pattern)
        row_result = check_rows(pattern)
        col_result = check_cols(pattern)
        if row_result!=None:
            # print('after row:',row_result)
            row_results.append(row_result+1)
            continue
        if col_result!=None:
            # print('after col:',col_result)
            col_results.append(col_result+1)
            continue
        # print('not found')
    return sum(col_results)+100*sum(row_results)

def check_rows_2(pattern):
    for i in range(1,pattern.shape[0]):
        l = min(i,pattern.shape[0]-i)
        sub_pattern_1 = pattern[i-l:i]
        sub_pattern_2 = pattern[i:i+l]
        print(np.sum(sub_pattern_1!=np.flipud(sub_pattern_2)))
        if np.sum(sub_pattern_1!=np.flipud(sub_pattern_2))==1:
             return i-1
    return None
def check_cols_2(pattern):
    for i in range(1,pattern.shape[1]):
        l = min(i,pattern.shape[1]-i)
        sub_pattern_1 = pattern[:,i-l:i]
        sub_pattern_2 = pattern[:,i:i+l]
        print(np.sum(sub_pattern_1!=np.fliplr(sub_pattern_2)))
        if np.sum(sub_pattern_1!=np.fliplr(sub_pattern_2))==1:
            return i-1
    return None
def part2(data):
    patterns_data = data.split('\n\n')
    patterns = [pattern_data.split('\n') for pattern_data in patterns_data]
    patterns[-1].remove('')
    patterns = [np.array([[*line] for line in pattern]) for pattern in patterns]

    row_results = []
    col_results = []
    for pattern in patterns:
        row_result = check_rows_2(pattern)
        col_result = check_cols_2(pattern)
        if row_result!=None:
            row_results.append(row_result+1)
            continue
        if col_result!=None:
            col_results.append(col_result+1)
            continue
    return sum(col_results)+100*sum(row_results)

if __name__=='__main__':
    data_dict =get_data(13,raw=True)
    data = data_dict['data.txt']

    result_part1 = part1(data)
    print("part1:",result_part1)

    result_part2 = part2(data)
    print("part2:",result_part2)
