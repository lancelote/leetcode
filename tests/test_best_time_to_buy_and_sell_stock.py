import pytest

from src.best_time_to_buy_and_sell_stock import Solution


@pytest.mark.parametrize(
    "prices,expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1], 0),
        ([2, 1, 2, 1, 0, 1, 2], 2),
    ],
)
def test_solution(prices, expected):
    assert Solution().maxProfit(prices) == expected
