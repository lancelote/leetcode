import pytest

from src.final_prices_with_a_special_discount_in_a_shop import Solution


@pytest.mark.parametrize(
    "prices,expected",
    (
        ([8, 4, 6, 2, 3], [4, 2, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([10, 1, 1, 6], [9, 0, 1, 6]),
    ),
)
def test_solution(prices, expected):
    assert Solution().finalPrices(prices) == expected
