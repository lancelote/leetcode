import pytest

from src.add_two_numbers import Solution
from src.utils.linked_list import to_linked_list
from src.utils.linked_list import to_list


@pytest.mark.parametrize(
    "in_list1,in_list2,out_list",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ([2, 4, 9], [5, 6, 4, 9], [7, 0, 4, 0, 1]),
    ],
)
def test_solution(in_list1, in_list2, out_list):
    l1 = to_linked_list(in_list1)
    l2 = to_linked_list(in_list2)

    assert to_list(Solution().addTwoNumbers(l1, l2)) == out_list
