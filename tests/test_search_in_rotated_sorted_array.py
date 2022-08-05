import pytest

from src.search_in_rotated_sorted_array import Solution


@pytest.mark.parametrize(
    "nums,targets,expected_index",
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([4, 5, 6, 7, 0, 1, 2], 7, 3),
        ([4, 5, 6, 7, 0, 1, 2], 4, 0),
        ([4, 5, 6, 7, 0, 1, 2], 2, 6),
        ([1], 1, 0),
        ([1, 3], 3, 1),
        ([1, 3], 0, -1),
        ([5, 1, 3], 3, 2),
    ],
)
def test_solution(nums, targets, expected_index):
    assert Solution().search(nums, targets) == expected_index
