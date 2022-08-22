import pytest

from src.power_of_four import Solution


@pytest.mark.parametrize(
    "n,expected",
    [
        (-4, False),
        (0, False),
        (1, True),
        (5, False),
        (4, True),
        (16, True),
    ],
)
def test_solution(n, expected):
    assert Solution().isPowerOfFour(n) is expected
