from src.utils.linked_list import ListNode


class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        less_head = less = ListNode()
        more_head = more = ListNode()

        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                more.next = head
                more = more.next
            head = head.next

        less.next = more_head.next
        more.next = None

        return less_head.next
