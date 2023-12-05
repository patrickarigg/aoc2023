from utils.data import get_data
from day4.day4 import part1, part2

data_dict = get_data(4)
test_data = data_dict['test_data.txt']

def test_day3_part1():
    assert part1(test_data)==13

def test_day3_part2():
    assert part2(test_data)==30
