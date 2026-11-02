from collections import deque

from src.utils.binary_tree import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        result: list[int] = []

        d: deque[TreeNode] = deque()
        d.append(root)

        while d:
            result.append(d[-1].val)

            for _ in range(len(d)):
                node = d.popleft()

                if node.left:
                    d.append(node.left)

                if node.right:
                    d.append(node.right)

        return result
