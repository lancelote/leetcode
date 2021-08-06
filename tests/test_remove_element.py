import pytest

from src.remove_element import Solution


@pytest.mark.parametrize(
    "nums,val,expected_elem_count,expected_arr",
    [
        ([3, 2, 2, 3], 3, 2, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4]),
    ],
)
def test_solution(nums, val, expected_elem_count, expected_arr):
    assert Solution().removeElement(nums, val) == expected_elem_count
    assert nums[:expected_elem_count] == expected_arr
