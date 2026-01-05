import pytest

from src.lowest_common_ancestor_of_a_binary_search_tree import Solution
from src.utils.binary_search_tree import list_to_tree
from src.utils.binary_search_tree import TreeNode


@pytest.mark.parametrize(
    "in_list,p_val,q_val,expected_val",
    [
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
        ([2, 1], 2, 1, 2),
    ],
)
def test_solution(in_list, p_val, q_val, expected_val):
    p = TreeNode(p_val)
    q = TreeNode(q_val)
    root = list_to_tree(in_list)

    assert root is not None
    assert Solution().lowestCommonAncestor(root, p, q).val == expected_val
