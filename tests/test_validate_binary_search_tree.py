import pytest

from src.utils.binary_search_tree import TreeNode
from src.validate_binary_search_tree import Solution


@pytest.mark.parametrize(
    "root,expected_validity",
    [
        (TreeNode(2, TreeNode(1), TreeNode(3)), True),
        (
            TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))),
            False,
        ),
        (
            TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7))),
            False,
        ),
    ],
)
def test_solution(root, expected_validity):
    assert Solution().isValidBST(root) is expected_validity
