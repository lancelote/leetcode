import pytest

from src.binary_tree_postorder_traversal import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,expected",
    (
        ([1, None, 2, 3], [3, 2, 1]),
        ([], []),
        ([1], [1]),
    ),
)
def test_solution(in_list, expected):
    root = list_to_tree(in_list)
    assert Solution().postorderTraversal(root) == expected
