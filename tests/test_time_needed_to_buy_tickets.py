import pytest

from src.time_needed_to_buy_tickets import Solution


@pytest.mark.parametrize(
    "tickets,k,expected",
    (
        ([2, 3, 2], 2, 6),
        ([5, 1, 1, 1], 0, 8),
    ),
)
def test_solution(tickets, k, expected):
    assert Solution().timeRequiredToBuy(tickets, k) == expected
