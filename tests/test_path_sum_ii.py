import pytest

from src.path_sum_ii import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list, target_sum, expected_paths",
    [
        (
            [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1],
            22,
            [[5, 4, 11, 2], [5, 8, 4, 5]],
        ),
        ([1, 2, 3], 5, []),
        ([1, 2], 0, []),
    ],
)
def test_solution(in_list, target_sum, expected_paths):
    root = list_to_tree(in_list)
    assert Solution().pathSum(root, target_sum) == expected_paths
