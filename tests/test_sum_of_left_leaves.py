import pytest

from src.sum_of_left_leaves import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,expected",
    (
        ([3, 9, 20, None, None, 15, 7], 24),
        ([1], 0),
    ),
)
def test_solution(in_list, expected):
    root = list_to_tree(in_list)
    assert Solution().sumOfLeftLeaves(root) == expected
