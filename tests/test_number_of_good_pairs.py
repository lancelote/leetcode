import pytest

from src.number_of_good_pairs import Solution


@pytest.mark.parametrize(
    "nums,good_pairs",
    [
        ([1, 2, 3, 1, 1, 3], 4),
        ([1, 1, 1, 1], 6),
        ([1, 2, 3], 0),
    ],
)
def test_solution(nums, good_pairs):
    assert Solution().numIdenticalPairs(nums) == good_pairs
