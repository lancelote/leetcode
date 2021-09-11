import pytest

from src.count_good_triplets import Solution


@pytest.mark.parametrize(
    "arr,a,b,c,expected",
    [
        ([3, 0, 1, 1, 9, 7], 7, 2, 3, 4),
        ([1, 1, 2, 2, 3], 0, 0, 1, 0),
    ],
)
def test_solution(arr, a, b, c, expected):
    assert Solution().countGoodTriplets(arr, a, b, c) == expected
