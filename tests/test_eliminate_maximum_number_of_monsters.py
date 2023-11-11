import pytest

from src.eliminate_maximum_number_of_monsters import Solution


@pytest.mark.parametrize(
    "dist,speed,expected",
    (
        ([1, 3, 4], [1, 1, 1], 3),
        ([1, 1, 2, 3], [1, 1, 1, 1], 1),
        ([3, 2, 4], [5, 3, 2], 1),
        ([3, 5, 7, 4, 5], [2, 3, 6, 3, 2], 2),
    ),
)
def test_solution(dist, speed, expected):
    assert Solution().eliminateMaximum(dist, speed) == expected
