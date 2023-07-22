import pytest

from src.check_if_array_is_good import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([2, 1, 3], False),
        ([1, 3, 3, 2], True),
        ([1, 1], True),
        ([3, 4, 4, 1, 2, 1], False),
        ([1], False),
        ([9, 9], False),
    ),
)
def test_solution(nums, expected):
    assert Solution().isGood(nums) is expected
