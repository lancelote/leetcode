import pytest

from src.symmetric_tree import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,expected",
    [
        ([1, 2, 2, 3, 4, 4, 3], True),
        ([1, 2, 2, None, 3, None, 3], False),
    ],
)
def test_solution(in_list, expected):
    root = list_to_tree(in_list)
    assert Solution().isSymmetric(root) is expected
