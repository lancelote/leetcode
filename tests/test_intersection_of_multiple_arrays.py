import pytest

from src.intersection_of_multiple_arrays import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]], [3, 4]),
        ([[1, 2, 3], [4, 5, 6]], []),
    ),
)
def test_solution(nums, expected):
    assert Solution().intersection(nums) == expected
