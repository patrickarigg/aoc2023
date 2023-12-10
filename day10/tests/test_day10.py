from utils.data import get_data
from day10.day10 import part1, part2
import pytest

data_dict = get_data(10)
test_data_1 = data_dict['test_data_1.txt']
test_data_2 = data_dict['test_data_2.txt']
test_data_3 = data_dict['test_data_3.txt']
test_data_4 = data_dict['test_data_4.txt']
test_data_5 = data_dict['test_data_5.txt']


def test_day10_part1_1():
    assert part1(test_data_1)==4

def test_day10_part1_2():
    assert part1(test_data_2)==8

def test_day10_part2_1():
    assert part2(test_data_3)==4

def test_day10_part2_2():
    assert part2(test_data_4)==8

def test_day10_part2_3():
    assert part2(test_data_5)==10
