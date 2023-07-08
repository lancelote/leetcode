import pytest

from src.number_of_black_blocks import Solution


@pytest.mark.parametrize(
    "m,n,coordinates,expected",
    (
        (3, 3, [[0, 0]], [3, 1, 0, 0, 0]),
        (3, 3, [[0, 0], [1, 1], [0, 2]], [0, 2, 2, 0, 0]),
    ),
)
def test_solution(m, n, coordinates, expected):
    assert Solution().countBlackBlocks(m, n, coordinates) == expected
