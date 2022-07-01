import pytest

from src.longest_consecutive_sequence import Solution


@pytest.mark.parametrize(
    "nums,expected_length",
    [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ],
)
def test_solution(nums, expected_length):
    assert Solution().longestConsecutive(nums) == expected_length
