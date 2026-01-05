from __future__ import annotations

import pytest

from src.convert_binary_number_in_a_linked_list_to_integer import Solution
from src.utils.linked_list import to_linked_list


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
    head = to_linked_list(items)

    assert head is not None
    assert Solution().getDecimalValue(head) == num
