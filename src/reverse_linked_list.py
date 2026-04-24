from src.utils.linked_list import ListNode


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        prev = head
        curr = head.next
        temp: ListNode | None = None

        prev.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
