import pytest

from src.integer_break import Solution


@pytest.mark.parametrize(
    "n,expected",
    (
        (2, 1),
        (10, 36),
        (3, 2),
        (4, 4),
    ),
)
def test_solution(n, expected):
    assert Solution().integerBreak(n) == expected
