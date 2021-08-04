from typing import Optional

import pytest

from src.merge_two_sorted_lists import ListNode
from src.merge_two_sorted_lists import Solution


def to_list(lst: list[int], i: int = 0) -> Optional[ListNode]:
    if i >= len(lst):
        return None
    else:
        return ListNode(val=lst[i], next=to_list(lst, i + 1))


def assert_list(l1: Optional[ListNode], l2: Optional[ListNode]) -> bool:
    if not l1 and not l2:
        return True
    elif not l1 or not l2:
        return False
    else:
        return l1.val == l2.val and assert_list(l1.next, l2.next)


@pytest.mark.parametrize(
    "l1,l2,expected",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ],
)
def test_solution(l1, l2, expected):
    result = Solution().mergeTwoLists(to_list(l1), to_list(l2))
    assert_list(result, to_list(expected))
