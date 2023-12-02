import re
from utils.data import get_data

def part1(data):
    total_sum = 0
    for line in data:
        nums = re.findall(r"\d",line)
        total_sum += int(nums[0]+nums[-1])
    return total_sum

def part2(data):
    #handle the number words
    numDict = {
        'nine':'9',
        'eight':'8',
        'seven':'7',
        'six':'6',
        'five':'5',
        'four':'4',
        'three':'3',
        'two':'2',
        'one':'1'
    }
    numDictReversed = {
        'enin':'9',
        'thgie':'8',
        'neves':'7',
        'xis':'6',
        'evif':'5',
        'ruof':'4',
        'eerht':'3',
        'owt':'2',
        'eno':'1'
    }
    total_sum = 0

    for line in data: #[::-1]
        #search from left
        lineReversed = line[::-1]
        first = re.findall(rf"\d|{'|'.join(numDict.keys())}",line)[0]
        last = re.findall(rf"\d|{'|'.join(numDictReversed.keys())}",lineReversed)[0]
        if first.isnumeric()==False:
            first=numDict[first]
        if last.isnumeric()==False:
            last=numDictReversed[last]
        total_sum += int(first+last)

    return total_sum

if __name__=='__main__':
    data_dict =get_data(1)
    data = data_dict['data.txt']
    #part1
    result_part1 = part1(data)
    print("part1:",result_part1)
    #part2
    result_part2 = part2(data)
    print("part2:",result_part2)
