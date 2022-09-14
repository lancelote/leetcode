import pytest

from src.pseudo_palindromic_paths_in_a_binary_tree import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,expected",
    [
        ([2, 3, 1, 3, 1, None, 1], 2),
        ([2, 1, 1, 1, 3, None, None, None, None, None, 1], 1),
        ([9], 1),
    ],
)
def test_solution(in_list, expected):
    root = list_to_tree(in_list)
    assert Solution().pseudoPalindromicPaths(root) == expected
