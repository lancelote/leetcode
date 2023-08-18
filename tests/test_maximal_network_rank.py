import pytest

from src.maximal_network_rank import Solution


@pytest.mark.parametrize(
    "n,roads,expected",
    (
        (4, [[0, 1], [0, 3], [1, 2], [1, 3]], 4),
        (5, [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]], 5),
        (8, [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]], 5),
    ),
)
def test_solutions(n, roads, expected):
    assert Solution().maximalNetworkRank(n, roads) == expected
