import pytest

from src.shortest_path_visiting_all_nodes import Solution


@pytest.mark.parametrize(
    "graph,expected",
    (
        ([[1, 2, 3], [0], [0], [0]], 4),
        ([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]], 4),
    ),
)
def test_solution(graph, expected):
    assert Solution().shortestPathLength(graph) == expected
