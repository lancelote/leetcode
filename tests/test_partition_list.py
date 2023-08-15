import pytest

from src.partition_list import Solution
from src.utils.linked_list import to_linked_list
from src.utils.linked_list import to_list


@pytest.mark.parametrize(
    "in_list,x,out_list",
    (
        ([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),
        ([2, 1], 2, [1, 2]),
    ),
)
def test_solution(in_list, x, out_list):
    head = to_linked_list(in_list)
    new_head = Solution().partition(head, x)
    assert to_list(new_head) == out_list
