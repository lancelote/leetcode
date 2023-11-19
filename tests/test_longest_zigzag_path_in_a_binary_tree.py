import pytest

from src.longest_zigzag_path_in_a_binary_tree import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,expected",
    (
        (
            [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1],
            3,
        ),
        ([1, 1, 1, None, 1, None, None, 1, 1, None, 1], 4),
    ),
)
def test_solution(in_list, expected):
    root = list_to_tree(in_list)
    assert Solution().longestZigZag(root) == expected
