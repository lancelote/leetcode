import pytest

from src.construct_binary_tree_from_inorder_and_postorder_traversal import (
    Solution,
)
from src.utils.binary_tree import tree_to_list


@pytest.mark.parametrize(
    "inorder,postorder,expected_out_list",
    (
        ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1]),
    ),
)
def test_solution(inorder, postorder, expected_out_list):
    out_tree = Solution().buildTree(inorder, postorder)
    assert tree_to_list(out_tree) == expected_out_list
