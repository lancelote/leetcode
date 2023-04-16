import pytest

from src.single_number import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
    ],
)
def test_solution(nums, expected):
    assert Solution().singleNumber(nums) == expected
