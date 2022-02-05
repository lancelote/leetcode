from typing import Optional

OptNode = Optional["ListNode"]


class ListNode:
    def __init__(self, val: int = 0, next: OptNode = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[OptNode]) -> OptNode:
        if not lists:
            return None

        while len(lists) > 1:
            merged_list = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_list.append(self.mergeLists(l1, l2))

            lists = merged_list

        return lists[0]

    def mergeLists(self, l1: OptNode, l2: OptNode) -> OptNode:
        dummy_head = ListNode()
        tail = dummy_head

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy_head.next
