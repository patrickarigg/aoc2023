from utils.data import get_data
from day2.day2 import part1, part2

data_dict = get_data(2)
test_data = data_dict['test_data.txt']

def test_day2_part1():
    assert part1(test_data)==8

def test_day2_part2():
    assert part2(test_data) == 2286
