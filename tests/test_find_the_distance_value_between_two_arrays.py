import pytest

from src.find_the_distance_value_between_two_arrays import Solution


@pytest.mark.parametrize(
    "arr1,arr2,d,expected",
    (
        ([4, 5, 8], [10, 9, 1, 8], 2, 2),
        ([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3, 2),
        ([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6, 1),
    ),
)
def test_solution(arr1, arr2, d, expected):
    assert Solution().findTheDistanceValue(arr1, arr2, d) == expected
