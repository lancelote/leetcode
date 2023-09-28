import pytest

from src.sort_array_by_parity import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([3, 1, 2, 4], [4, 2, 1, 3]),
        ([0], [0]),
    ),
)
def test_solution(nums, expected):
    assert Solution().sortArrayByParity(nums) == expected
