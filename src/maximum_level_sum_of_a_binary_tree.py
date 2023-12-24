import sys
from collections import deque

from src.utils.binary_tree import TreeNode


class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        max_total = -sys.maxsize
        max_level = 1

        level = 1

        d: deque[TreeNode] = deque()
        if root:
            d.append(root)

        while d:
            level_sum = 0

            for _ in range(len(d)):
                node = d.popleft()
                level_sum += node.val

                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)

            if level_sum > max_total:
                max_total = level_sum
                max_level = level

            level += 1

        return max_level
