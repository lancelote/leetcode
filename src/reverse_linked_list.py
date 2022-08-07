from src.utils.linked_list import ListNode


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev: ListNode | None = None
        current = head

        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp

        return prev
