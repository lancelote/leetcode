from __future__ import annotations

import pytest

from src.convert_binary_number_in_a_linked_list_to_integer import Solution
from src.utils.linked_list import ListNode


def to_list_node(items: list[int], i: int = 0) -> ListNode | None:
    if i == len(items):
        return None
    return ListNode(items[i], to_list_node(items, i + 1))


@pytest.mark.parametrize(
    "items,num",
    [
        ([1, 0, 1], 5),
        ([0], 0),
        ([1], 1),
        ([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], 18880),
        ([0, 0], 0),
    ],
)
def test_solution(items, num):
    assert Solution().getDecimalValue(to_list_node(items)) == num
