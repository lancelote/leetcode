from src.utils.binary_tree import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        max_depth = 0
        stack: list[tuple[TreeNode | None, int]] = [(root, 1)]

        while stack:
            node, depth = stack.pop()

            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return max_depth
