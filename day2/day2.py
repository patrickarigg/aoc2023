from utils.data import get_data
import re

def part1(data):
    max_values = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    possible_games = []
    for game_data in data:
        game_index = int(re.findall(r"^Game (\d+):",game_data)[0])
        draws = re.findall(r"^.+:(.+)",game_data)[0].split(';')
        possible_draws = []
        for draw in draws:
            reds = re.findall(r"(\d+) red",draw)
            greens = re.findall(r"(\d+) green",draw)
            blues = re.findall(r"(\d+) blue",draw)
            freq_dict = {
                'red': int(reds[0]) if reds else 0,
                'green': int(greens[0]) if greens else 0,
                'blue': int(blues[0]) if blues else 0
            }
            possible_draw = all([freq_dict[key]<=max_values[key] for key in freq_dict])
            possible_draws.append(possible_draw)
        possible = all(possible_draws)
        if possible:
            possible_games.append(game_index)

    return sum(possible_games)

def part2(data):
    powers = []
    for game_data in data:
        draws = re.findall(r"^.+:(.+)",game_data)[0].split(';')
        game_freqs = []
        for draw in draws:
            reds = re.findall(r"(\d+) red",draw)
            greens = re.findall(r"(\d+) green",draw)
            blues = re.findall(r"(\d+) blue",draw)
            freq_dict = {
                'red': int(reds[0]) if reds else 0,
                'green': int(greens[0]) if greens else 0,
                'blue': int(blues[0]) if blues else 0
            }
            game_freqs.append(freq_dict)

        red_max = max(map(lambda x: x.get('red',0),game_freqs))
        green_max = max(map(lambda x: x.get('green',0),game_freqs))
        blue_max = max(map(lambda x: x.get('blue',0),game_freqs))
        powers.append(red_max*green_max*blue_max)

    return sum(powers)

if __name__=='__main__':
    data_dict =get_data(2)
    data = data_dict['data.txt']

    result_part1 = part1(data)
    print("part1:",result_part1)

    result_part2 = part2(data)
    print("part2:",result_part2)
