import pytest

from src.merge_k_sorted_lists import Solution
from src.utils.linked_list import to_linked_list
from src.utils.linked_list import to_list


@pytest.mark.parametrize(
    "l1_array,l2_array,expected_list",
    [
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2], [3], [1, 2, 3]),
    ],
)
def test_merge_lists(l1_array, l2_array, expected_list):
    l1 = to_linked_list(l1_array)
    l2 = to_linked_list(l2_array)

    assert to_list(Solution().mergeLists(l1, l2)) == expected_list


@pytest.mark.parametrize(
    "lists,expected_list",
    [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
    ],
)
def test_solution(lists, expected_list):
    heads = [to_linked_list(x) for x in lists]
    assert to_list(Solution().mergeKLists(heads)) == expected_list
