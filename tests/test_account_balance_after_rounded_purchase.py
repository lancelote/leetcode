import pytest

from src.account_balance_after_rounded_purchase import Solution


@pytest.mark.parametrize(
    "purchase_amount,expected",
    (
        (9, 90),
        (15, 80),
    ),
)
def test_solution(purchase_amount, expected):
    assert Solution().accountBalanceAfterPurchase(purchase_amount) == expected
