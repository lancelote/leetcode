import pytest

from src.add_two_integers import Solution


@pytest.mark.parametrize(
    "num1,num2,expected",
    [
        (12, 5, 17),
        (-10, 4, -6),
    ],
)
def test_solution(num1, num2, expected):
    assert Solution().sum(num1, num2) == expected
