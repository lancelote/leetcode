import pytest

from src.two_sum_iv_input_is_a_bst import Solution
from src.utils.binary_search_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,k,expected",
    [
        ([5, 3, 6, 2, 4, None, 7], 9, True),
        ([5, 3, 6, 2, 4, None, 7], 28, False),
    ],
)
def test_solution(in_list, k, expected):
    root = list_to_tree(in_list)
    assert Solution().findTarget(root, k) is expected
