from utils.data import get_data
from day13.day13 import part1, part2
import pytest

data_dict = get_data(13,raw=True)
test_data = data_dict['test_data.txt']

def test_day13_part1():
    assert part1(test_data)==405

pytest.mark.skip()
def test_dayx_part2():
    pass
