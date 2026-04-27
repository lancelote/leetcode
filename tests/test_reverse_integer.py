import pytest

from src.reverse_integer import Solution


@pytest.mark.parametrize(
    "x,expected",
    [
        (123, 321),
        (-123, -321),
        (0, 0),
        (1534236469, 0),
        (-2147483412, -2143847412),
        (-2147483648, 0),
        (1463847412, 2147483641),
    ],
)
def test_solution(x, expected):
    assert Solution().reverse(x) == expected
