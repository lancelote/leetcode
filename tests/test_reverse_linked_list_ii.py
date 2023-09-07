import pytest

from src.reverse_linked_list_ii import Solution
from src.utils.linked_list import to_linked_list
from src.utils.linked_list import to_list


@pytest.mark.parametrize(
    "in_list,left,right,expected_out_list",
    (
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
        ([5], 1, 1, [5]),
    ),
)
def test_solution(in_list, left, right, expected_out_list):
    head = to_linked_list(in_list)
    out = Solution().reverseBetween(head, left, right)
    assert to_list(out) == expected_out_list
