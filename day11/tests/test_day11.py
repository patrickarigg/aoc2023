from utils.data import get_data
from day11.day11 import part1, part2, calculate_distance
import pytest

data_dict = get_data(11)
test_data = data_dict['test_data.txt']

galaxies = [(0, 4), (1, 9), (2, 0), (5, 8), (6, 1), (7, 12), (10, 9), (11, 0), (11, 5)]

def test_day11_part1():
    assert part1(test_data)==374

def test_calculate_distance():
    assert calculate_distance(galaxies[0],galaxies[6])==15
    assert calculate_distance(galaxies[2],galaxies[5])==17
    assert calculate_distance(galaxies[7],galaxies[8])==5

# pytest.mark.skip()
def test_day11_part2():
    assert part2(test_data,2)==374
    assert part2(test_data,10)==1030
