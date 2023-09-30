import pytest

from src._132_pattern import Solution


@pytest.mark.parametrize(
    "nums,is_expected_pattern",
    [
        ([1, 2, 3, 4], False),
        ([3, 1, 4, 2], True),
        ([-1, 3, 2, 0], True),
        ([3, 5, 0, 3, 4], True),
    ],
)
def test_solution(nums, is_expected_pattern):
    assert Solution().find132pattern(nums) == is_expected_pattern
