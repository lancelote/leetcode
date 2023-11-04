import pytest

from src.last_moment_before_all_ants_fall_out_of_a_plank import Solution


@pytest.mark.parametrize(
    "n,left,right,expected",
    (
        (4, [4, 3], [0, 1], 4),
        (7, [], [0, 1, 2, 3, 4, 5, 6, 7], 7),
        (7, [0, 1, 2, 3, 4, 5, 6, 7], [], 7),
        (5, [], [], 0),
    ),
)
def test_solution(n, left, right, expected):
    assert Solution().getLastMoment(n, left, right) == expected
