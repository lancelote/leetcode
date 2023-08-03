import pytest

from src.n_th_tribonacci_number import Solution


@pytest.mark.parametrize(
    "n,expected",
    (
        (4, 4),
        (25, 1389537),
        (3, 2),
    ),
)
def test_solution(n, expected):
    assert Solution().tribonacci(n) == expected
