import pytest

from src.next_permutation import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),
        ([1, 5, 1], [5, 1, 1]),
    ),
)
def test_solution(nums, expected):
    Solution().nextPermutation(nums)
    assert nums == expected
