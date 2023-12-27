import pytest

from src.number_of_provinces import Solution


@pytest.mark.parametrize(
    "is_connected,expected",
    (
        ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
    ),
)
def test_solution(is_connected, expected):
    assert Solution().findCircleNum(is_connected) == expected
