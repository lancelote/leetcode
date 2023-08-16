import pytest

from src.sliding_window_maximum import Solution


@pytest.mark.parametrize(
    "nums,k,expected",
    (
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
        ([1, -1], 1, [1, -1]),
    ),
)
def test_solution(nums, k, expected):
    assert Solution().maxSlidingWindow(nums, k) == expected
