from src.utils.linked_list import ListNode


def get_len(root: ListNode | None) -> int:
    length = 0

    while root:
        length += 1
        root = root.next

    return length


class Solution:
    def getIntersectionNode(
        self, head_a: ListNode, head_b: ListNode
    ) -> ListNode | None:
        len_a = get_len(head_a)
        len_b = get_len(head_b)
        diff = abs(len_a - len_b)

        if len_a > len_b:
            for _ in range(diff):
                assert head_a.next
                head_a = head_a.next
        else:
            for _ in range(diff):
                assert head_b.next
                head_b = head_b.next

        while head_a != head_b:
            assert head_a.next and head_b.next
            head_a = head_a.next
            head_b = head_b.next

        return head_a
