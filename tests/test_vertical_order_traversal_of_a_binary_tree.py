import pytest

from src.utils.binary_tree import list_to_tree
from src.vertical_order_traversal_of_a_binary_tree import Solution


@pytest.mark.parametrize(
    "in_list,expected_traversal",
    [
        ([3, 9, 20, None, None, 15, 7], [[9], [3, 15], [20], [7]]),
        ([1, 2, 3, 4, 5, 6, 7], [[4], [2], [1, 5, 6], [3], [7]]),
        ([1, 2, 3, 4, 6, 5, 7], [[4], [2], [1, 5, 6], [3], [7]]),
        ([3, 1, 4, 0, 2, 2], [[0], [1], [3, 2, 2], [4]]),
    ],
)
def test_solution(in_list, expected_traversal):
    root = list_to_tree(in_list)
    assert Solution().verticalTraversal(root) == expected_traversal
