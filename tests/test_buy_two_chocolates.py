import pytest

from src.buy_two_chocolates import Solution


@pytest.mark.parametrize(
    "prices,money,expected",
    (
        (
            [1, 2, 2],
            3,
            0,
        ),
        (
            [3, 2, 3],
            3,
            3,
        ),
        ([98, 54, 6, 34, 66, 63, 52, 39], 62, 22),
    ),
)
def test_solution(prices, money, expected):
    assert Solution().buyChoco(prices, money) == expected
