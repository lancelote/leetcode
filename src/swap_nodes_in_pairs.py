from utils.linked_list import ListNode


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head

        before = dummy

        while before.next and before.next.next:
            a = before.next
            b = a.next
            after = b.next

            a.next = after
            b.next = a
            before.next = b

            before = a

        return dummy.next
