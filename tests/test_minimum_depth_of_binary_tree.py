import pytest

from src.minimum_depth_of_binary_tree import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,expected",
    (
        ([3, 9, 20, None, None, 15, 7], 2),
        ([2, None, 3, None, 4, None, 5, None, 6], 5),
        ([1], 1),
        ([], 0),
    ),
)
def test_solution(in_list, expected):
    root = list_to_tree(in_list)
    assert Solution().minDepth(root) == expected
