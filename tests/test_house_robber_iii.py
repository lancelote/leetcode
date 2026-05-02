import pytest

from src.utils.binary_tree import list_to_tree
from src.house_robber_iii import Solution


@pytest.mark.parametrize(
    "in_list,expected",
    (
        ([3, 2, 3, None, 3, None, 1], 7),
        ([3, 4, 5, 1, 3, None, 1], 9),
    ),
)
def test_solution(in_list, expected):
    root = list_to_tree(in_list)
    assert Solution().rob(root) == expected
