import pytest

from src.find_the_highest_altitude import Solution


@pytest.mark.parametrize(
    "gain,expected",
    [
        ([-5, 1, 5, 0, -7], 1),
        ([-4, -3, -2, -1, 4, 3, 2], 0),
    ],
)
def test_solution(gain, expected):
    assert Solution().largestAltitude(gain) == expected
