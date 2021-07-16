import pytest

from src.sum_of_all_odd_length_subarrays import Solution


@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 4, 2, 5, 3], 58),
        ([1, 2], 3),
        ([10, 11, 12], 66),
    ],
)
def test_solution(arr, expected):
    assert Solution().sumOddLengthSubarrays(arr) == expected
