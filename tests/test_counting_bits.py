import pytest

from src.counting_bits import Solution


@pytest.mark.parametrize(
    "n,expected",
    [
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
    ],
)
def test_solution(n, expected):
    assert Solution().countBits(n) == expected
