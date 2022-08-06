from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


def to_linked_list(array: list[int], i: int = 0) -> ListNode | None:
    if i == len(array):
        return None
    return ListNode(val=array[i], next=to_linked_list(array, i + 1))


def assert_linked_list(l1: ListNode | None, l2: ListNode | None) -> bool:
    if not l1 and not l2:
        return True
    elif not l1 or not l2:
        return False
    else:
        return l1.val == l2.val and assert_linked_list(l1.next, l2.next)


def to_list(head: ListNode | None) -> list[int]:
    result = []

    while head is not None:
        result.append(head.val)
        head = head.next

    return result


__all__ = ["ListNode", "to_linked_list", "assert_linked_list", "to_list"]
