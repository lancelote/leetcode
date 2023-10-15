import pytest

from src.number_of_ways_to_stay_in_the_same_place_after_some_steps import (
    Solution,
)


@pytest.mark.parametrize(
    "steps,arr_len,expected",
    (
        (3, 2, 4),
        (2, 4, 2),
        (4, 2, 8),
        (27, 7, 127784505),
    ),
)
def test_solution(steps, arr_len, expected):
    assert Solution().numWays(steps, arr_len) == expected
