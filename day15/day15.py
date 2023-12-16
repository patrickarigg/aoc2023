from utils.data import get_data
import re

def hash(string):
    value=0
    for char in string:
        # Determine the ASCII code for the current character of the string.
        ascii_val = ord(char)
        # Increase the current value by the ASCII code you just determined.
        value+=ascii_val
        # Set the current value to itself multiplied by 17.
        value=value*17
        # Set the current value to the remainder of dividing itself by 256.
        value = value % 256
    return value

def part1(data):
    steps = data.split('\n')[0].split(',')
    hash_results = []
    for step in steps:
        value = hash(step)
        hash_results.append(value)
    return sum(hash_results)
def part2(data):
    boxes = {i:[] for i in range(256)}
    steps = data.split('\n')[0].split(',')
    for step in steps:
        label = re.findall(r"(.+)[=-]",step)[0]
        box_number=hash(label)
        op = re.findall(r"[=-]",step)[0]
        if op=='-':
            #remove the lens with the given label
            for lens in boxes[box_number]:
                if lens[0]==label:
                    boxes[box_number].remove(lens)
                    break
        if op=='=':
            lens_swapped=False
            new_focus_length = re.findall(r"[=-](\d)",step)[0]
            for lens in boxes[box_number]:
                if lens[0]==label:
                    lens[1]=new_focus_length
                    lens_swapped=True
                    break
            if lens_swapped:
                continue
            boxes[box_number].append([label,new_focus_length])
    total = 0
    for i in range(256):
        if boxes[i]:
            for index, lens in enumerate(boxes[i]):
                power = (1 + i) * (index+1) * int(lens[1])
                total+=power
    return total

if __name__=='__main__':
    data_dict =get_data(15,raw=True)
    data = data_dict['data.txt']

    result_part1 = part1(data)
    print("part1:",result_part1)

    result_part2 = part2(data)
    print("part2:",result_part2)
