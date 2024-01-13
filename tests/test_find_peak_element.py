import pytest

from src.find_peak_element import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([1, 2, 3, 1], 2),
        ([1, 2, 1, 3, 5, 6, 4], 5),
    ),
)
def test_solution(nums, expected):
    assert Solution().findPeakElement(nums) == expected
