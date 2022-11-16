import pytest

from src.count_complete_tree_nodes import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,expected",
    [
        ([1, 2, 3, 4, 5, 6], 6),
        ([], 0),
        ([1], 1),
    ],
)
def test_solution(in_list, expected):
    root = list_to_tree(in_list)
    assert Solution().countNodes(root) == expected
