import pytest

from src.frequency_of_the_most_frequent_element import Solution


@pytest.mark.parametrize(
    "nums,k,expected",
    (
        ([1, 2, 4], 5, 3),
        ([1, 4, 8, 13], 5, 2),
        ([3, 9, 6], 2, 1),
    ),
)
def test_solution(nums, k, expected):
    assert Solution().maxFrequency(nums, k) == expected
