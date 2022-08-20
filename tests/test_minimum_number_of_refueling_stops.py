import pytest

from src.minimum_number_of_refueling_stops import Solution


@pytest.mark.parametrize(
    "target,cur_fuel,stations,expected",
    [
        (1, 1, [], 0),
        (100, 1, [[10, 100]], -1),
        (100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]], 2),
    ],
)
def test_solution(target, cur_fuel, stations, expected):
    assert Solution().minRefuelStops(target, cur_fuel, stations) == expected
