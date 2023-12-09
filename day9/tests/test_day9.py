import pytest
from utils.data import get_data
from day9.day9 import part1, part2, get_next_el

data_dict = get_data(9)
test_data = data_dict['test_data.txt']

def test_day9_part1_1():
    assert get_next_el(test_data[0])==18

def test_day9_part1_2():
    assert get_next_el(test_data[1])==28

def test_day9_part1_3():
    assert get_next_el(test_data[2])==68

def test_day9_part1():
    assert part1(test_data)==114

def test_day9_part2():
    assert part2([test_data[-1]])==5
