import pytest

from src.binary_tree_pruning import Solution
from src.utils.binary_tree import list_to_tree
from src.utils.binary_tree import tree_to_list


@pytest.mark.parametrize(
    "in_list,expected_out_list",
    [
        ([1, None, 0, 0, 1], [1, None, 0, None, 1]),
        ([1, 0, 1, 0, 0, 0, 1], [1, None, 1, None, 1]),
        ([1, 1, 0, 1, 1, 0, 1, 0], [1, 1, 0, 1, 1, None, 1]),
        ([], []),
        ([0], []),
        ([0, 1], [0, 1]),
    ],
)
def test_solution(in_list, expected_out_list):
    root = list_to_tree(in_list)
    result_root = Solution().pruneTree(root)
    assert tree_to_list(result_root) == expected_out_list
