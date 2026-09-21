import pytest

from src.find_x_value_of_array_i import Solution


@pytest.mark.parametrize(
    "nums,k,expected",
    (
        ([1, 2, 3, 4, 5], 3, [9, 2, 4]),
        ([1, 2, 4, 8, 16, 32], 4, [18, 1, 2, 0]),
        ([1, 1, 2, 1, 1], 2, [9, 6]),
    ),
)
def test_solution(nums, k, expected):
    assert Solution().resultArray(nums, k) == expected
