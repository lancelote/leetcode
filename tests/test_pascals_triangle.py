import pytest

from src.pascals_triangle import Solution


@pytest.mark.parametrize(
    "num_rows,expected",
    (
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (1, [[1]]),
    ),
)
def test_solution(num_rows, expected):
    assert Solution().generate(num_rows) == expected
