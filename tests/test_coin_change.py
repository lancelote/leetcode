import pytest

from src.coin_change import Solution


@pytest.mark.parametrize(
    "coins,amount,expected_count",
    [
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
    ],
)
def test_solution(coins, amount, expected_count):
    assert Solution().coinChange(coins, amount) == expected_count
