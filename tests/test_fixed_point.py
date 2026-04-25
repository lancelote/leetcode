import pytest

from src.fixed_point import Solution


@pytest.mark.parametrize(
    "arr,expected",
    (
        ([-10, -5, 0, 3, 7], 3),
        ([0, 2, 5, 8, 17], 0),
        ([-10, -5, 3, 4, 7, 9], -1),
    ),
)
def test_solution(arr, expected):
    assert Solution().fixedPoint(arr) == expected
