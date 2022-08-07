import pytest

from src.reverse_linked_list import Solution
from src.utils.linked_list import to_linked_list
from src.utils.linked_list import to_list


@pytest.mark.parametrize(
    "in_list,out_list",
    [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
    ],
)
def test_solution(in_list, out_list):
    head = to_linked_list(in_list)
    assert to_list(Solution().reverseList(head)) == out_list
