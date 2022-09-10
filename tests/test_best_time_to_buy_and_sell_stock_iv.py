import pytest

from src.best_time_to_buy_and_sell_stock_iv import Solution


@pytest.mark.parametrize(
    "k,prices,expected_profit",
    [
        (2, [5, 11, 3, 50, 60, 90], 93),
        (2, [2, 4, 1], 2),
        (2, [3, 2, 6, 5, 0, 3], 7),
        (5, [1, 2], 1),
        (2, [], 0),
    ],
)
def test_solution(k, prices, expected_profit):
    assert Solution().maxProfit(k, prices) == expected_profit
