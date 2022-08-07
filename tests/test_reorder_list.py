import pytest

from src.reorder_list import Solution
from src.utils.linked_list import to_linked_list
from src.utils.linked_list import to_list


@pytest.mark.parametrize(
    "in_list,expected_out_list",
    [
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1], [1]),
    ],
)
def test_solution(in_list, expected_out_list):
    head = to_linked_list(in_list)
    Solution().reorderList(head)
    assert to_list(head) == expected_out_list
