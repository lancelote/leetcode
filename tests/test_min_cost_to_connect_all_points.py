import pytest

from src.min_cost_to_connect_all_points import Solution


@pytest.mark.parametrize(
    "data,expected",
    (
        ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20),
        ([[3, 12], [-2, 5], [-4, 1]], 18),
    ),
)
def test_solution(data, expected):
    assert Solution().minCostConnectPoints(data) == expected
