import pytest

from src.minimum_cost_to_reach_city_with_discounts import Solution


@pytest.mark.parametrize(
    "n,highways,discounts,expected",
    (
        (5, [[0, 1, 4], [2, 1, 3], [1, 4, 11], [3, 2, 3], [3, 4, 2]], 1, 9),
        (4, [[1, 3, 17], [1, 2, 7], [3, 2, 5], [0, 1, 6], [3, 0, 20]], 20, 8),
        (4, [[0, 1, 3], [2, 3, 2]], 0, -1),
        (5, [[0, 1, 0], [2, 1, 0], [1, 4, 11], [3, 2, 0], [3, 4, 0]], 4, 0),
        (5, [[0, 1, 4], [1, 2, 3], [2, 3, 0], [0, 3, 8], [3, 4, 100]], 2, 54),
    ),
)
def test_solution(n, highways, discounts, expected):
    assert Solution().minimumCost(n, highways, discounts) == expected
