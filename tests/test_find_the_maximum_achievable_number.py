import pytest

from src.find_the_maximum_achievable_number import Solution


@pytest.mark.parametrize(
    "num,t,expected",
    (
        (4, 1, 6),
        (3, 2, 7),
    ),
)
def test_solution(num, t, expected):
    assert Solution().theMaximumAchievableX(num, t) == expected
