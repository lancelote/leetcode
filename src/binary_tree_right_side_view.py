from collections import deque

from src.utils.binary_tree import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        right_view: list[int] = []
        queue = deque([root])

        while queue:
            node: TreeNode | None = None

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if node:
                right_view.append(node.val)

        return right_view
