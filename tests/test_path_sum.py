import pytest

from src.path_sum import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,target_sum,expected",
    [
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True),
        ([1, 2, 3], 5, False),
        ([], 0, False),
        ([1, 2], 1, False),
        ([-2, None, -3], -5, True),
    ],
)
def test_solution(in_list, target_sum, expected):
    root = list_to_tree(in_list)
    assert Solution().hasPathSum(root, target_sum) is expected
