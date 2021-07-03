import pytest
from src.find_center_of_star_graph import Solution


@pytest.mark.parametrize(
    "edges,center",
    [([[1, 2], [2, 3], [4, 2]], 2), ([[1, 2], [5, 1], [1, 3], [1, 4]], 1)],
)
def test_solution(edges, center):
    assert Solution().findCenter(edges) == center
