import pytest

from src.utils.binary_tree import find_node
from src.utils.binary_tree import list_to_tree
from src.utils.binary_tree import tree_to_list
from src.utils.binary_tree import TreeNode


@pytest.mark.parametrize(
    "tree,expected_list",
    (
        (None, []),
        (TreeNode(1, left=None, right=TreeNode(2)), [1, None, 2]),
        (
            TreeNode(
                3,
                TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))),
                TreeNode(5),
            ),
            [3, 4, 5, 1, 2, None, None, None, None, 0],
        ),
        (TreeNode(1, TreeNode(2)), [1, 2]),
    ),
)
def test_tree_to_list(tree, expected_list):
    assert tree_to_list(tree) == expected_list


@pytest.mark.parametrize(
    "in_list,out_list",
    (
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, None, 2], [1, None, 2]),
        (
            [3, 4, 5, 1, 2, None, None, None, None, 0],
            [3, 4, 5, 1, 2, None, None, None, None, 0],
        ),
        ([None, 1, 2, 3], []),
    ),
)
def test_list_to_tree(in_list, out_list):
    out_tree = list_to_tree(in_list)
    assert tree_to_list(out_tree) == out_list


class TestListToTree:
    def test_not_full_last_layer(self):
        lst = [3, 4, 5, 1, 2]
        tree = list_to_tree(lst)

        assert tree is not None
        assert tree.val == 3

        assert tree.left is not None
        assert tree.left.val == 4

        assert tree.right is not None
        assert tree.right.val == 5

        assert tree.left.left is not None
        assert tree.left.left.val == 1

        assert tree.left.right is not None
        assert tree.left.right.val == 2

        assert tree.right.left is None
        assert tree.right.right is None


def test_find_node():
    tree = TreeNode(0, TreeNode(1), TreeNode(2))

    node_0 = tree
    node_1 = tree.left
    node_2 = tree.right

    assert find_node(tree, 0) is node_0
    assert find_node(tree, 1) is node_1
    assert find_node(tree, 2) is node_2
