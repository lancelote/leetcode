import pytest

from src.reverse_integer import Solution


@pytest.mark.parametrize(
    "x,expected",
    [
        (123, 321),
        (-123, -321),
        (0, 0),
    ],
)
def test_solution(x, expected):
    assert Solution().reverse(x) == expected
