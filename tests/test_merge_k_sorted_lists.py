import pytest

from src.merge_k_sorted_lists import Solution
from src.utils.linked_list import is_equal
from src.utils.linked_list import to_linked_list


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
    expected_head = to_linked_list(expected_list)

    assert is_equal(Solution().mergeKLists(heads), expected_head)
