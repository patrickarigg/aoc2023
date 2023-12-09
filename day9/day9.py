from utils.data import get_data

def get_next_el(row_data):
    seq = list(map(int,row_data.split(' ')))
    sub_seq = seq.copy()
    diffs_arr = [sub_seq]
    while(True):
        diffs = []
        for i in range(len(sub_seq)-1):
            diffs.append(sub_seq[i+1]-sub_seq[i])
        diffs_arr.append(diffs)
        if all(x==0 for x in diffs):
            break
        sub_seq=diffs

    diffs_arr.reverse()

    for i in range(len(diffs_arr)): #i = 0,1,2
        if i==0:
            diffs_arr[i].append(0)
            continue
        diffs_arr[i].append(diffs_arr[i][-1]+diffs_arr[i-1][-1])

    return diffs_arr[-1][-1]

def get_previous_el(row_data):
    seq = list(map(int,row_data.split(' ')))
    sub_seq = seq.copy()
    diffs_arr = [sub_seq]
    while(True):
        diffs = []
        for i in range(len(sub_seq)-1):
            diffs.append(sub_seq[i+1]-sub_seq[i])
        diffs_arr.append(diffs)
        if all(x==0 for x in diffs):
            break
        sub_seq=diffs

    diffs_arr.reverse()
    for i in range(len(diffs_arr)):
        if i==0:
            diffs_arr[i].insert(0,0)
            continue
        diffs_arr[i].insert(0,diffs_arr[i][0]-diffs_arr[i-1][0])

    return diffs_arr[-1][0]

def part1(data):
    results = []
    for row_data in data:
        results.append(get_next_el(row_data))
    return sum(results)

def part2(data):
    results = []
    for row_data in data:
        results.append(get_previous_el(row_data))
    return sum(results)

if __name__=='__main__':
    data_dict =get_data(9)
    data = data_dict['data.txt']

    result_part1 = part1(data)
    print("part1:",result_part1)

    result_part2 = part2(data)
    print("part2:",result_part2)
