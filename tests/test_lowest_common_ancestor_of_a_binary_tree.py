import pytest

from src.lowest_common_ancestor_of_a_binary_tree import Solution
from src.utils.binary_tree import list_to_tree
from src.utils.binary_tree import TreeNode


@pytest.mark.parametrize(
    "in_list,p_val,q_val,expected_val",
    (
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),
        ([1, 2], 1, 2, 1),
    ),
)
def test_solution(in_list, p_val, q_val, expected_val):
    root = list_to_tree(in_list)
    p = TreeNode(p_val)
    q = TreeNode(q_val)

    assert root is not None

    result = Solution().lowestCommonAncestor(root, p, q)

    assert result is not None
    assert result.val == expected_val
