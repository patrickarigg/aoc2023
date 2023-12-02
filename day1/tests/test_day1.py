from utils.data import get_data
from day1.day1 import part1, part2

data_dict = get_data(1)
test_data_1 = data_dict['test_data_1.txt']
test_data_2 = data_dict['test_data_2.txt']

def test_day1_part1():
    assert part1(test_data_1)==142

def test_day1_part2():
    assert part2(test_data_2)==281
