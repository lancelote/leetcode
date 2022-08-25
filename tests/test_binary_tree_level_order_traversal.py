import pytest

from src.binary_tree_level_order_traversal import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,expected_levels",
    [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),
    ],
)
def test_solution(in_list, expected_levels):
    root = list_to_tree(in_list)
    assert Solution().levelOrder(root) == expected_levels
