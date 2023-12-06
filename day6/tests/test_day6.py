from utils.data import get_data
from day6.day6 import part1, part2

data_dict = get_data(6)
test_data = data_dict['test_data.txt']

def test_dayx_part1():
    assert part1(test_data)==288

def test_dayx_part2():
    assert part2(test_data)==71503
