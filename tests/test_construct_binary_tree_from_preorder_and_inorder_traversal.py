import pytest

from src.construct_binary_tree_from_preorder_and_inorder_traversal import (
    Solution,
)
from src.utils.binary_tree import tree_to_list


@pytest.mark.parametrize(
    "preorder,inorder,out_list",
    [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1]),
    ],
)
def test_solution(preorder, inorder, out_list):
    out_tree = Solution().buildTree(preorder, inorder)
    assert tree_to_list(out_tree) == out_list
