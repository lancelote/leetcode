import pytest

from src.count_number_of_bad_pairs import Solution


@pytest.mark.parametrize(
    "nums,expected_pairs",
    [
        ([4, 1, 3, 3], 5),
        ([1, 2, 3, 4, 5], 0),
    ],
)
def test_solution(nums, expected_pairs):
    assert Solution().countBadPairs(nums) == expected_pairs
