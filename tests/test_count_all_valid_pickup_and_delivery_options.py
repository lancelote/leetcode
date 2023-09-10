import pytest

from src.count_all_valid_pickup_and_delivery_options import Solution


@pytest.mark.parametrize(
    "n,expected",
    (
        (1, 1),
        (2, 6),
    ),
)
def test_solution(n, expected):
    assert Solution().countOrders(n) == expected
