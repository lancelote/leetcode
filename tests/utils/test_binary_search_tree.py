import pytest

from src.utils.binary_search_tree import insert
from src.utils.binary_search_tree import list_to_tree
from src.utils.binary_search_tree import tree_to_list
from src.utils.binary_search_tree import TreeNode


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


@pytest.mark.parametrize(
    "in_list,insert_value,out_list",
    [
        ([0], None, [0]),
        ([2, 1], 3, [2, 1, 3]),
        ([2, 1, 3], 0, [2, 1, 3, 0]),
        ([2, 3], 1, [2, 1, 3]),
    ],
)
def test_insert(in_list, insert_value, out_list):
    in_tree = list_to_tree(in_list)
    result_tree = insert(in_tree, insert_value)
    result_list = tree_to_list(result_tree)
    assert result_list == out_list


@pytest.mark.parametrize(
    "in_list",
    [
        ([]),
        ([2, 1, 3]),
        ([0]),
        ([2, 3]),
    ],
)
def test_list_to_tree(in_list):
    assert tree_to_list(list_to_tree(in_list)) == in_list
