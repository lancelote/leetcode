import pytest

from src.maximum_level_sum_of_a_binary_tree import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,expected",
    (
        ([1, 7, 0, 7, -8, None, None], 2),
        ([989, None, 10250, 98693, -89388, None, None, None, -32127], 2),
        ([-100, -200, -300, -20, -5, -10, None], 3),
    ),
)
def test_solution(in_list, expected):
    root = list_to_tree(in_list)
    assert Solution().maxLevelSum(root) == expected
