import pytest

from src.cells_with_odd_values_in_a_matrix import Solution


@pytest.mark.parametrize(
    "m,n,indices,expected_odd",
    [
        (2, 3, [[0, 1], [1, 1]], 6),
        (2, 2, [[1, 1], [0, 0]], 0),
    ],
)
def test_solution(m, n, indices, expected_odd):
    assert Solution().oddCells(m, n, indices) == expected_odd
