import pytest

from src.utils.binary_tree import list_to_tree
from src.utils.binary_tree import tree_to_list
from src.utils.binary_tree import TreeNode


@pytest.mark.parametrize(
    "tree,expected_list",
    [
        (None, []),
        (TreeNode(1, left=None, right=TreeNode(2)), [1, None, 2]),
    ],
)
def test_tree_to_list(tree, expected_list):
    assert tree_to_list(tree) == expected_list


@pytest.mark.parametrize(
    "in_list,out_list",
    [
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2, None]),
        ([1, None, 2], [1, None, 2]),
    ],
)
def test_list_to_tree(in_list, out_list):
    out_tree = list_to_tree(in_list)
    assert tree_to_list(out_tree) == out_list
