import pytest

from src.remove_duplicates_from_sorted_list_ii import Solution
from src.utils.linked_list import to_linked_list
from src.utils.linked_list import to_list


@pytest.mark.parametrize(
    "in_list,expected_out_list",
    (
        ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
        ([1, 1, 1, 2, 3], [2, 3]),
    ),
)
def test_solution(in_list, expected_out_list):
    head = to_linked_list(in_list)
    out_head = Solution().deleteDuplicates(head)
    out_list = to_list(out_head)
    assert out_list == expected_out_list
