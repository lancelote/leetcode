from __future__ import annotations

from collections import deque


class Node:
    def __init__(
        self,
        val: int = 0,
        left: Node | None = None,
        right: Node | None = None,
        next: Node | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node | None) -> Node | None:
        if not root:
            return None

        queue: deque[Node] = deque()
        queue.append(root)

        while queue:
            for i in range(len(queue) - 1):
                queue[i].next = queue[i + 1]
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root
