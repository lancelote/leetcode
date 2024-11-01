from src.utils.linked_list import ListNode


def get_len(head: ListNode | None) -> int:
    result = 0

    while head:
        result += 1
        head = head.next

    return result


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if k == 1:
            return head

        dummy = ListNode(next=head)
        n = get_len(head)

        last_end = dummy
        left = dummy.next
        assert left
        right = left.next

        for _ in range(n // k):
            for _ in range(k - 1):
                assert right
                tmp = right.next
                right.next = left
                left = right
                right = tmp

            tmp = last_end.next
            last_end.next = left
            assert tmp
            last_end = tmp
            last_end.next = right

            left = right
            right = right.next if right else None

        return dummy.next
