import pytest

from src.binary_tree_inorder_traversal import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,expected_traversal",
    [
        ([1, None, 2, 3], [1, 3, 2]),
        ([], []),
        ([1], [1]),
    ],
)
def test_solution(in_list, expected_traversal):
    root = list_to_tree(in_list)
    assert Solution().inorderTraversal(root) == expected_traversal
