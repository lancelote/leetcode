import pytest

from src.smallest_even_multiple import Solution


@pytest.mark.parametrize(
    "n,expected",
    (
        (5, 10),
        (6, 6),
    ),
)
def test_solution(n, expected):
    assert Solution().smallestEvenMultiple(n) == expected
