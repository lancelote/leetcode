import pytest

from src.minimum_money_required_before_transactions import Solution


@pytest.mark.parametrize(
    "transactions,expected_money",
    [
        ([[2, 1], [5, 0], [4, 2]], 10),
        ([[3, 0], [0, 3]], 3),
        ([[3, 1], [2, 3]], 4),
        ([[3, 2], [1, 3]], 3),
    ],
)
def test_solution(transactions, expected_money):
    assert Solution().minimumMoney(transactions) == expected_money
