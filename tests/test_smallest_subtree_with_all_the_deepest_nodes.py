import pytest

from src.smallest_subtree_with_all_the_deepest_nodes import Solution
from src.utils.binary_tree import list_to_tree
from src.utils.binary_tree import tree_to_list


@pytest.mark.parametrize(
    "in_list,out_list",
    (
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], [2, 7, 4]),
        ([1], [1]),
        ([0, 1, 3, None, 2], [2]),
    ),
)
def test_solution(in_list, out_list):
    root = list_to_tree(in_list)
    actual = Solution().subtreeWithAllDeepest(root)
    assert tree_to_list(actual) == out_list
