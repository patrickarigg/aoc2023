from utils.data import get_data
from day8.day8 import part1, part2

data_dict = get_data(8)
test_data_1 = data_dict['test_data_1.txt']
test_data_2 = data_dict['test_data_2.txt']
test_data_3 = data_dict['test_data_3.txt']

def test_day8_part1_1():
    assert part1(test_data_1)==2

def test_day8_part1_2():
    assert part1(test_data_2)==6

def test_day8_part2():
    assert part2(test_data_3)==6
