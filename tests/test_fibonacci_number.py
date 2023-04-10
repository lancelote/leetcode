import pytest

from src.fibonacci_number import Solution


@pytest.mark.parametrize(
    "n,expected",
    [
        (2, 1),
        (3, 2),
        (4, 3),
    ],
)
def test_solution(n, expected):
    assert Solution().fib(n) == expected
