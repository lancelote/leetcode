import pytest

from src.best_time_to_buy_and_sell_stock_ii import Solution


@pytest.mark.parametrize(
    "prices,expected_profit",
    (
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
    ),
)
def test_solution(prices, expected_profit):
    assert Solution().maxProfit(prices) == expected_profit
