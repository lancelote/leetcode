import pytest

from src.concatenation_of_array import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 1], [1, 2, 1, 1, 2, 1]),
        ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1]),
    ],
)
def test_solution(nums, expected):
    assert Solution().getConcatenation(nums) == expected
