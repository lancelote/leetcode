import pytest

from src.minimum_cost_for_tickets import Solution


@pytest.mark.parametrize(
    "days,costs,expected",
    (
        ([1, 4, 6, 7, 8, 20], [2, 7, 15], 11),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17),
    ),
)
def test_solution(days, costs, expected):
    assert Solution().mincostTickets(days, costs) == expected
