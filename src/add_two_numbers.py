from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


def list_to_int(lst: ListNode | None) -> int:
    stack: list[str] = []

    while lst:
        stack.append(str(lst.val))
        lst = lst.next

    return int("".join(stack)[::-1])


def int_to_list(num: int) -> ListNode:
    dummy = ListNode(-1)
    current = dummy

    for val in (int(x) for x in str(num)[::-1]):
        node = ListNode(val)

        assert current
        current.next = node
        current = current.next

    assert dummy.next
    return dummy.next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        n1 = list_to_int(l1)
        n2 = list_to_int(l2)

        return int_to_list(n1 + n2)
