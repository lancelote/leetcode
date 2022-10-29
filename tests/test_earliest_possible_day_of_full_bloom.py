import pytest

from src.earliest_possible_day_of_full_bloom import Solution


@pytest.mark.parametrize(
    "plant_time,grow_time,expected_day",
    [
        ([1, 4, 3], [2, 3, 1], 9),
        ([1, 2, 3, 2], [2, 1, 2, 1], 9),
        ([1], [1], 2),
    ],
)
def test_solution(plant_time, grow_time, expected_day):
    assert Solution().earliestFullBloom(plant_time, grow_time) == expected_day
