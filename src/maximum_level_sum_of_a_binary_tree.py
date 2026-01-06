from collections import deque

from src.utils.binary_tree import TreeNode


class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        if root is None:
            raise ValueError("root is None")

        max_level_n = 1
        max_sum = root.val

        level_n = 1
        to_visit: deque[TreeNode] = deque([root])

        while to_visit:
            level_sum = 0

            for _ in range(len(to_visit)):
                node = to_visit.popleft()
                level_sum += node.val

                if node.left is not None:
                    to_visit.append(node.left)

                if node.right is not None:
                    to_visit.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level_n = level_n

            level_n += 1

        return max_level_n
