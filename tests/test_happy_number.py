import pytest

from src.happy_number import Solution


@pytest.mark.parametrize(
    "expected,n",
    (
        (True, 19),
        (False, 2),
    ),
)
def test_solution(expected, n):
    assert expected is Solution().isHappy(n)
