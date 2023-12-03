from utils.data import get_data
import re

def part1(data):
    parts =[]
    for row in range(len(data)):
        #find all nums on a row and their start and end index
        nums = re.findall(r"\d+",data[row])
        num_locations = [match.span() for match in re.finditer(r"\d+",data[row])]

        #check if they are valid - i.e have a special char next to one of the digits
        for i in range(len(num_locations)):
            if is_valid_part(row,num_locations[i],data):
                parts.append(int(nums[i]))

    return sum(parts)


def part2(data):
    #find all nums on a row and their start and end index
    all_num_locations = [] #[(row,(col_start,col_end),...]
    for row in range(len(data)):
        num_locations = [(row,match.span()) for match in re.finditer(r"\d+",data[row])]
        all_num_locations+=num_locations

    #find possible gears
    possible_gears = []
    for row in range(len(data)):
        gear_locations = [(row,match.start()) for match in re.finditer(r"\*",data[row])]
        possible_gears+=gear_locations

    #find gear ratios
    gear_ratios = get_gear_ratios(possible_gears,all_num_locations,data)

    return sum(gear_ratios)

def is_special_char(char):
    match = re.search(r"[^0-9.]",char)
    if match:
        return True
    return False

def is_valid_part(row,num_location,data):
    i = row
    for j in range(num_location[0],num_location[1]):
        surrounding_locations = [(i,j-1),(i-1, j-1),(i-1, j),(i-1, j+1),(i, j+1),(i+1, j+1),(i+1, j),(i+1, j-1)]
        for loc in surrounding_locations:
            r=loc[0]
            c=loc[1]
            if r>=0 and c>=0 and r<len(data) and c<len(data[0]) and is_special_char(data[r][c]):
                return True
    return False

def get_gear_ratios(possible_gears,all_num_locations,data):
    gear_ratios = []
    for gear_location in possible_gears:
        values = []
        i = gear_location[0]
        j = gear_location[1]
        surrounding_locations = [(i,j-1),(i-1, j-1),(i-1, j),(i-1, j+1),(i, j+1),(i+1, j+1),(i+1, j),(i+1, j-1)]
        for loc in surrounding_locations:
            r=loc[0]
            c=loc[1]
            num, num_location = get_num_in_location(r,c,all_num_locations,data)
            if num_location:
                all_num_locations.remove(num_location)
            values.append(num)
        values = [value for value in values if value!=None]
        if len(values)==2:
            gear_ratios.append(values[0]*values[1])
    return gear_ratios

def get_num_in_location(i,j,all_num_locations,data):
    for num_location in all_num_locations:
        if i==num_location[0] and (j in list(range(num_location[1][0],num_location[1][1]))):
            return int(data[num_location[0]][num_location[1][0]:num_location[1][1]]), num_location
    return None, None

if __name__=='__main__':
    data_dict =get_data(3)
    data = data_dict['data.txt']

    result_part1 = part1(data)
    print("part1:",result_part1)

    result_part2 = part2(data)
    print("part2:",result_part2)
