from utils.data import get_data
import re

def part1(data):
    times = [int(i) for i in re.findall(r"\d+",data[0])]
    record_distances = [int(i) for i in re.findall(r"\d+",data[1])]

    race_results = []

    for time, record_distance in zip(times,record_distances):
        n_ways = 0
        for time_held in range(1,time): #dont need to check 0 and time
            speed = time_held
            time_left = time-time_held

            dist = speed*time_left
            if dist>record_distance:
                n_ways+=1
        race_results.append(n_ways)

    total = 1
    for race_result in race_results:
        total*=race_result

    return total

def part2(data):
    time = int(''.join(re.findall(r"\d+",data[0])))
    record_distance = int(''.join(re.findall(r"\d+",data[1])))

    n_ways = 0
    for time_held in range(1,time): #dont need to check 0 and time
        speed = time_held
        time_left = time-time_held

        dist = speed*time_left
        if dist>record_distance:
            n_ways+=1

    return n_ways

if __name__=='__main__':
    data_dict =get_data(6)
    data = data_dict['data.txt']

    result_part1 = part1(data)
    print("part1:",result_part1)

    result_part2 = part2(data)
    print("part2:",result_part2)
