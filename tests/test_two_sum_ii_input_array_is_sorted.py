import pytest

from src.two_sum_ii_input_array_is_sorted import Solution


@pytest.mark.parametrize(
    "numbers,target,expected",
    [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
    ],
)
def test_solution(numbers, target, expected):
    assert Solution().twoSum(numbers, target) == expected
