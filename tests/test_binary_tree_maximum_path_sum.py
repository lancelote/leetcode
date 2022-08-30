import pytest

from src.binary_tree_maximum_path_sum import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,expected_path",
    [
        ([1, 2, 3], 6),
        ([-10, 9, 20, None, None, 15, 7], 42),
        ([2, -1], 2),
        ([1, -2, -3, 1, 3, -2, None, -1], 3),
    ],
)
def test_solution(in_list, expected_path):
    root = list_to_tree(in_list)
    assert Solution().maxPathSum(root) == expected_path
