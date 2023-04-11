import pytest

from src.convert_sorted_array_to_binary_search_tree import Solution
from src.utils.binary_search_tree import tree_to_list


@pytest.mark.parametrize(
    "nums,out_list",
    [
        ([-10, -3, 0, 5, 9], [0, -3, 9, -10, 5]),
        ([1, 3], [3, 1]),
    ],
)
def test_solution(nums, out_list):
    out_tree = Solution().sortedArrayToBST(nums)
    assert tree_to_list(out_tree) == out_list
