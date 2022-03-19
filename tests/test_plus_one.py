import pytest

from src.plus_one import Solution


@pytest.mark.parametrize(
    "digits,after_increment",
    [
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([9], [1, 0]),
    ],
)
def test_solution(digits, after_increment):
    assert Solution().plusOne(digits) == after_increment
