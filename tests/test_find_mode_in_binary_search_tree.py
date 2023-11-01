import pytest

from src.find_mode_in_binary_search_tree import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,expected",
    (
        ([1, None, 2, 2], [2]),
        ([0], [0]),
    ),
)
def test_solution(in_list, expected):
    root = list_to_tree(in_list)
    assert Solution().findMode(root) == expected
