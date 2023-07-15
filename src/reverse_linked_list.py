from src.utils.linked_list import ListNode


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        previous = None

        while head:
            tmp = head.next
            head.next = previous
            previous = head
            head = tmp

        return previous
