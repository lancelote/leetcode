import pytest

from src.power_of_three import Solution


@pytest.mark.parametrize(
    "n,expected",
    [
        (-1, False),
        (0, False),
        (1, True),
        (2, False),
        (3, True),
        (26, False),
        (27, True),
        (28, False),
    ],
)
def test_solution(n, expected):
    assert Solution().isPowerOfThree(n) is expected
