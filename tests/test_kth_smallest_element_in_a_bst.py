import pytest

from src.kth_smallest_element_in_a_bst import Solution
from src.utils.binary_search_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,k,expected_val",
    [
        ([3, 1, 4, None, 2], 1, 1),
        ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
    ],
)
def test_solution(in_list, k, expected_val):
    root = list_to_tree(in_list)
    assert Solution().kthSmallest(root, k) == expected_val
