import pytest

from src.find_target_indices_after_sorting_array import Solution


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([1, 2, 5, 2, 3], 2, [1, 2]),
        ([1, 2, 5, 2, 3], 3, [3]),
        ([1, 2, 5, 2, 3], 5, [4]),
    ],
)
def test_solution(nums, target, expected):
    assert Solution().targetIndices(nums, target) == expected
