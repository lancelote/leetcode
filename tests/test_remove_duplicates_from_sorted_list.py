import pytest

from src.remove_duplicates_from_sorted_list import Solution
from src.utils.linked_list import to_linked_list
from src.utils.linked_list import to_list


@pytest.mark.parametrize(
    "head_lst,result_lst",
    [
        ([1, 1, 2], [1, 2]),
        ([1, 1, 2, 3, 3], [1, 2, 3]),
    ],
)
def test_solution(head_lst, result_lst):
    head_node = to_linked_list(head_lst)
    result_node = Solution().deleteDuplicates(head_node)
    assert to_list(result_node) == result_lst
