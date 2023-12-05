from utils.data import get_data

def part1():
    pass

def part2():
    pass

if __name__=='__main__':
    data_dict =get_data(4)
    data = data_dict['data.txt']

    result_part1 = part1(data)
    print("part1:",result_part1)

    result_part2 = part2(data)
    print("part2:",result_part2)
