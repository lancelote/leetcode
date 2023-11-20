import pytest

from src.minimum_amount_of_time_to_collect_garbage import Solution


@pytest.mark.parametrize(
    "garbage,travel,expected",
    (
        (["G", "P", "GP", "GG"], [2, 4, 3], 21),
        (["MMM", "PGM", "GP"], [3, 10], 37),
    ),
)
def test_solution(garbage, travel, expected):
    assert Solution().garbageCollection(garbage, travel) == expected
