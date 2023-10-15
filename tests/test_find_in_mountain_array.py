import pytest

from src.find_in_mountain_array import MountainArray
from src.find_in_mountain_array import Solution


@pytest.mark.parametrize(
    "target,mountain_array,expected",
    (
        (3, MountainArray([1, 2, 3, 4, 5, 3, 1]), 2),
        (3, MountainArray([0, 1, 2, 4, 2, 1]), -1),
        (1, MountainArray([1, 5, 2]), 0),
        (2, MountainArray([1, 5, 2]), 2),
        (0, MountainArray([1, 2, 5, 1]), -1),
    ),
)
def test_solution(target, mountain_array, expected):
    assert Solution().findInMountainArray(target, mountain_array) == expected
