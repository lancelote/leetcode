import pytest

from src.number_of_connected_components_in_an_undirected_graph import Solution


@pytest.mark.parametrize(
    "n,edges,expected",
    [
        (5, [[0, 1], [1, 2], [3, 4]], 2),
    ],
)
def test_solution(n, edges, expected):
    assert Solution().countConnected(n, edges) == expected
