import pytest

from src.path_sum_iii import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,target_sum,expected",
    (
        ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8, 3),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, 3),
        ([1, -2, -3, 1, 3, -2, None, -1], 3, 1),
    ),
)
def test_solution(in_list, target_sum, expected):
    root = list_to_tree(in_list)
    assert Solution().pathSum(root, target_sum) == expected
