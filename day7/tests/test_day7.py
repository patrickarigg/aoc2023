from utils.data import get_data
from day7.day7 import part1, part2

data_dict = get_data(7)
test_data = data_dict['test_data.txt']
test_data_2 = data_dict['test_data_2.txt']

def test_day7_part1():
    assert part1(test_data)==6440

def test_day7_part1_2():
    assert part1(test_data_2)==6592

def test_day7_part2():
    assert part2(test_data)==5905
