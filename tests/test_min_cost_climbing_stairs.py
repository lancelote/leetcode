import pytest

from src.min_cost_climbing_stairs import Solution


@pytest.mark.parametrize(
    "cost,expected",
    (
        ([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
    ),
)
def test_solution(cost, expected):
    assert Solution().minCostClimbingStairs(cost) == expected
