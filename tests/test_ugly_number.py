import pytest

from src.ugly_number import Solution


@pytest.mark.parametrize(
    "n,expected",
    [
        (0, False),
        (6, True),
        (1, True),
        (14, False),
    ],
)
def test_solution(n, expected):
    assert Solution().isUgly(n) == expected
