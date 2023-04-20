import pytest

from src.balanced_binary_tree import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,expected",
    [
        ([3, 9, 20, None, None, 15, 7], True),
        ([1, 2, 2, 3, 3, None, None, 4, 4], False),
        ([], True),
    ],
)
def test_solution(in_list, expected):
    root = list_to_tree(in_list)
    assert Solution().isBalanced(root) is expected
