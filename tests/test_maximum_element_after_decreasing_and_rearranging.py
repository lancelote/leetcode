import pytest

from src.maximum_element_after_decreasing_and_rearranging import Solution


@pytest.mark.parametrize(
    "arr,expected",
    (
        ([2, 2, 1, 2, 1], 2),
        ([100, 1, 1000], 3),
        ([1, 2, 3, 4, 5], 5),
    ),
)
def test_solution(arr, expected):
    assert (
        Solution().maximumElementAfterDecrementingAndRearranging(arr)
        == expected
    )
