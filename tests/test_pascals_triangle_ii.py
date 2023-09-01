import pytest

from src.pascals_triangle_ii import Solution


@pytest.mark.parametrize(
    "row_index,expected",
    (
        (3, [1, 3, 3, 1]),
        (0, [1]),
        (1, [1, 1]),
    ),
)
def test_solution(row_index, expected):
    assert Solution().getRow(row_index) == expected
