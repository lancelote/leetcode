import pytest

from src.binary_tree_paths import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,expected",
    (
        ([1, 2, 3, None, 5], ["1->2->5", "1->3"]),
        ([1], ["1"]),
    ),
)
def test_solution(in_list, expected):
    root = list_to_tree(in_list)
    assert Solution().binaryTreePaths(root) == expected
