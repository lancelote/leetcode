import pytest

from src.monotonic_array import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([1, 2, 2, 3], True),
        ([6, 5, 4, 4], True),
        ([1, 3, 2], False),
    ),
)
def test_solution(nums, expected):
    assert Solution().isMonotonic(nums) is expected
