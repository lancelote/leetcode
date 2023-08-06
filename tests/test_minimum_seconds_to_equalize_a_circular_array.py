import pytest

from src.minimum_seconds_to_equalize_a_circular_array import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([1, 2, 1, 2], 1),
        ([2, 1, 3, 3, 2], 2),
        ([5, 5, 5, 5], 0),
        ([4, 18], 1),
        ([4, 3, 3], 1),
        ([8, 8, 9, 10, 9], 1),
        ([7, 19, 7, 17, 19, 19], 1),
        ([8, 10, 9, 20, 15, 17, 15, 20, 8, 18], 3),
        ([8, 14, 10, 6, 7, 11, 12, 20, 7, 17, 10], 3),
    ),
)
def test_solution(nums, expected):
    assert Solution().minimumSeconds(nums) == expected
