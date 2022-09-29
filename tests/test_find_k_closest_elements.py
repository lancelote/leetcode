import pytest

from src.find_k_closest_elements import Solution


@pytest.mark.parametrize(
    "arr,k,x,expected",
    [
        ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4]),
    ],
)
def test_solution(arr, k, x, expected):
    assert Solution().findClosestElements(arr, k, x) == expected
