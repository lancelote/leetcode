import pytest

from src.delete_the_middle_node_of_a_linked_list import Solution
from src.utils.linked_list import to_linked_list
from src.utils.linked_list import to_list


@pytest.mark.parametrize(
    "in_list,out_list",
    [
        ([1, 3, 4, 7, 1, 2, 6], [1, 3, 4, 1, 2, 6]),
        ([1, 2, 3, 4], [1, 2, 4]),
        ([2, 1], [2]),
        ([1], []),
    ],
)
def test_solution(in_list, out_list):
    head = to_linked_list(in_list)
    new_head = Solution().deleteMiddle(head)
    assert to_list(new_head) == out_list
