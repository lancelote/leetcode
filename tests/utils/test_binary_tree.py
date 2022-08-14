import pytest

from src.utils.binary_tree import tree_to_list
from src.utils.binary_tree import TreeNode


@pytest.mark.parametrize(
    "tree,expected_list",
    [
        (None, []),
        (TreeNode(42), [42]),
        (TreeNode(1, TreeNode(2), TreeNode(3)), [1, 2, 3]),
        (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)), [1, 2, 3, 4]),
    ],
)
def test_tree_to_list(tree, expected_list):
    assert tree_to_list(tree) == expected_list
