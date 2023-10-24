import pytest

from src.find_largest_value_in_each_tree_row import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,expected",
    (
        ([1, 3, 2, 5, 3, None, 9], [1, 3, 9]),
        ([1, 2, 3], [1, 3]),
    ),
)
def test_solution(in_list, expected):
    root = list_to_tree(in_list)
    assert Solution().largestValues(root) == expected
