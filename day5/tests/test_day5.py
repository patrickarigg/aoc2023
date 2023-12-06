from utils.data import get_data
from day5.day5 import part1, part2
import pytest

data_dict = get_data(5)
test_data = data_dict['test_data.txt']

def test_day5_part1():
    assert part1(test_data)==35

@pytest.mark.skip(reason="not implemented part2")
def test_day5_part2():
    pass
