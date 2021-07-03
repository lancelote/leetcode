import pytest
from src.range_sum_of_bst import create_tree
from src.range_sum_of_bst import Solution


@pytest.mark.parametrize(
    "root,low,high,total",
    [
        (create_tree([10, 5, 15, 3, 7, 18]), 7, 15, 32),
        (create_tree([10, 5, 15, 3, 7, 13, 18, 1, 6]), 6, 10, 23),
    ],
)
def test_solution(root, low, high, total):
    assert Solution().rangeSumBST(root, low, high) == total
