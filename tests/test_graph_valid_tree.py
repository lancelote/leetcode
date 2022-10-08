import pytest

from src.graph_valid_tree import Solution


@pytest.mark.parametrize(
    "n,edges,expected",
    [
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
        (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),
    ],
)
def test_solution(n, edges, expected):
    assert Solution().valid_tree(n, edges) == expected
