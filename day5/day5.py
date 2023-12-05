from utils.data import get_data
import re

def get_seed_data(data):
    data_string = '\n'.join(data)

    seed_data = re.search(r"seeds: (([\d+ ])+)",data_string).group(1).split(' ')
    seeds = [int(seed) for seed in seed_data]
    # print(seeds)

    seed_to_soil_data = re.search(r"seed-to-soil map:\n((([\d+ ])+\n)+)",data_string).group(1).split('\n')[:-1]
    seed_to_soil_data = [el.split(' ') for el in seed_to_soil_data]
    seed_to_soil = [[int(el) for el in line] for line in seed_to_soil_data]
    # print(seed_to_soil)

    soil_to_fertilizer_data = re.search(r"soil-to-fertilizer map:\n((([\d+ ])+\n)+)",data_string).group(1).split('\n')[:-1]
    soil_to_fertilizer_data = [el.split(' ') for el in soil_to_fertilizer_data]
    soil_to_fertilizer = [[int(el) for el in line] for line in soil_to_fertilizer_data]
    # print(soil_to_fertilizer)

    fertilizer_to_water_data = re.search(r"fertilizer-to-water map:\n((([\d+ ])+\n)+)",data_string).group(1).split('\n')[:-1]
    fertilizer_to_water_data = [el.split(' ') for el in fertilizer_to_water_data]
    fertilizer_to_water = [[int(el) for el in line] for line in fertilizer_to_water_data]
    # print(fertilizer_to_water)

    water_to_light_data = re.search(r"water-to-light map:\n((([\d+ ])+\n)+)",data_string).group(1).split('\n')[:-1]
    water_to_light_data = [el.split(' ') for el in water_to_light_data]
    water_to_light = [[int(el) for el in line] for line in water_to_light_data]
    # print(water_to_light)

    light_to_temperature_data = re.search(r"light-to-temperature map:\n((([\d+ ])+\n)+)",data_string).group(1).split('\n')[:-1]
    light_to_temperature_data = [el.split(' ') for el in light_to_temperature_data]
    light_to_temperature = [[int(el) for el in line] for line in light_to_temperature_data]
    # print(light_to_temperature)

    temperature_to_humidity_data = re.search(r"temperature-to-humidity map:\n((([\d+ ])+\n)+)",data_string).group(1).split('\n')[:-1]
    temperature_to_humidity_data = [el.split(' ') for el in temperature_to_humidity_data]
    temperature_to_humidity = [[int(el) for el in line] for line in temperature_to_humidity_data]
    # print(temperature_to_humidity)

    humidity_to_location_data = re.search(r"humidity-to-location map:\n((([\d+ ])+\n*)+)",data_string).group(1).split('\n')
    humidity_to_location_data = [el.split(' ') for el in humidity_to_location_data][:-1]
    humidity_to_location = [[int(el) for el in line] for line in humidity_to_location_data]
    # print(humidity_to_location)

    return seeds,seed_to_soil,soil_to_fertilizer,fertilizer_to_water,water_to_light,light_to_temperature,temperature_to_humidity,humidity_to_location

def get_map(map_data):
    def map_func(key):
        for line in map_data:
            d_start, s_start, length = line
            if key in range(s_start,s_start+length):
                return d_start+(key-s_start)
        return key
    return map_func

def remove_overalapping_ranges(seed_ranges):
    seed_ranges.sort(key=lambda tup: tup[0])
    new_ranges = []
    current_min = seed_ranges[0][0]

    for i in range(len(seed_ranges)-1):
        if seed_ranges[i][1]<seed_ranges[i+1][0]:
            new_ranges.append((current_min,seed_ranges[i][1]))
            current_min=seed_ranges[i+1][0]

    return new_ranges


def part1(data):
    (seeds,
     seed_to_soil,
     soil_to_fertilizer,
     fertilizer_to_water,
     water_to_light,
     light_to_temperature,
     temperature_to_humidity,
     humidity_to_location) = get_seed_data(data)
    # seeds: 79 14 55 13

    seed_to_soil_map = get_map(seed_to_soil)
    soil_to_fertilizer_map = get_map(soil_to_fertilizer)
    fertilizer_to_water_map = get_map(fertilizer_to_water)
    water_to_light_map = get_map(water_to_light)
    light_to_temperature_map = get_map(light_to_temperature)
    temperature_to_humidity_map = get_map(temperature_to_humidity)
    humidity_to_location_map = get_map(humidity_to_location)

    locations = []
    for seed in seeds:
        soil = seed_to_soil_map(seed)
        fertilizer = soil_to_fertilizer_map(soil)
        water = fertilizer_to_water_map(fertilizer)
        light = water_to_light_map(water)
        temperature = light_to_temperature_map(light)
        humidity = temperature_to_humidity_map(temperature)
        location = humidity_to_location_map(humidity)
        locations.append(location)

    return min(locations)

def part2(data):
    pass

if __name__=='__main__':
    data_dict =get_data(5)
    data = data_dict['data.txt']

    result_part1 = part1(data)
    print("part1:",result_part1)

    result_part2 = part2(data)
    print("part2:",result_part2)
