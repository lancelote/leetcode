import pytest

from src.determine_if_a_cell_is_reachable_at_a_given_time import Solution


@pytest.mark.parametrize(
    "sx,sy,fx,fy,t,expected",
    (
        (2, 4, 7, 7, 6, True),
        (3, 1, 7, 3, 3, False),
        (1, 1, 1, 3, 2, True),
        (1, 2, 1, 2, 1, False),
    ),
)
def test_solution(sx, sy, fx, fy, t, expected):
    assert Solution().isReachableAtTime(sx, sy, fx, fy, t) is expected
