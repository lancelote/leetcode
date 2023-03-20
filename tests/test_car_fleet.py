import pytest

from src.car_fleet import Solution


@pytest.mark.parametrize(
    "target,positions,speeds,expected",
    [
        (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),
        (10, [3], [3], 1),
        (100, [0, 2, 4], [4, 2, 1], 1),
        (10, [0, 2], [1, 1], 2),
        (10, [3, 5, 7], [3, 2, 1], 1),
    ],
)
def test_solution(target, positions, speeds, expected):
    assert Solution().carFleet(target, positions, speeds) == expected
