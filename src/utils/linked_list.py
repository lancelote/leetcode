from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


def to_linked_list(array: list[int]) -> ListNode | None:
    if not array:
        return None

    dummy = ListNode()
    tail = dummy

    for x in array:
        tail.next = ListNode(x)
        tail = tail.next

    return dummy.next


def is_equal(l1: ListNode | None, l2: ListNode | None) -> bool:
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next

    return l1 is None and l2 is None


def to_list(head: ListNode | None) -> list[int]:
    result = []

    while head is not None:
        result.append(head.val)
        head = head.next

    return result


__all__ = ["ListNode", "to_linked_list", "is_equal", "to_list"]
