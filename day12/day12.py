from utils.data import get_data

def part1(data):
    springs, nums = data[0].split(" ")
    nums = list(map(int,nums.split(',')))
    print(springs)
    print(nums)
    for loc in springs:
        # if it's a . go to the next character.
        if loc=='.':
            continue
        # if it's a # go to the next character, while reducing 1 from the first element in the nums list
        if loc=='#':
            nums[0]-=1
            if nums[0]==0:
                nums.pop(0)
            continue
        # if it's a ? branch make assumption and use backtracking if not valid



def part2(data):
    pass

if __name__=='__main__':
    data_dict =get_data(12)
    data = data_dict['test_data.txt']

    result_part1 = part1(data)
    print("part1:",result_part1)

    result_part2 = part2(data)
    print("part2:",result_part2)
