import pytest

from src.the_k_weakest_rows_in_a_matrix import Solution


@pytest.mark.parametrize(
    "mat,k,expected",
    (
        (
            [
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 1],
            ],
            3,
            [2, 0, 3],
        ),
        (
            [[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]],
            2,
            [0, 2],
        ),
    ),
)
def test_solution(mat, k, expected):
    assert Solution().kWeakestRows(mat, k) == expected
