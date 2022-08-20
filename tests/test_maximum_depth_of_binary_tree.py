import pytest

from src.maximum_depth_of_binary_tree import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,expected_max_depth",
    [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([], 0),
        ([1, None, 2], 2),
    ],
)
def test_solution(in_list, expected_max_depth):
    in_tree = list_to_tree(in_list)
    assert Solution().maxDepth(in_tree) == expected_max_depth
