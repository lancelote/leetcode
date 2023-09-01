import sys

from src.utils.binary_tree import TreeNode


class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        def dfs(node: TreeNode | None) -> int:
            if not node:
                return sys.maxsize
            if not node.left and not node.right:
                return 1
            return 1 + min(dfs(node.left), dfs(node.right))

        return dfs(root)
