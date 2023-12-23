from collections import deque

from src.utils.binary_tree import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        result: list[int] = []
        d: deque[TreeNode] = deque()

        if root:
            d.append(root)

        while d:
            result.append(0)

            for _ in range(len(d)):
                node = d.popleft()
                result[-1] = node.val

                if node.left:
                    d.append(node.left)

                if node.right:
                    d.append(node.right)

        return result
