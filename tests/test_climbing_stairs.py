import pytest

from src.climbing_stairs import Solution


@pytest.mark.parametrize(
    "n,expected",
    [
        (2, 2),
        (3, 3),
        (5, 8),
    ],
)
def test_solution(n, expected):
    assert Solution().climbStairs(n) == expected
