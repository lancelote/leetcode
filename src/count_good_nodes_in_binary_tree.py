from src.utils.binary_tree import TreeNode


class Solution:
    def goodNodes(self, head: TreeNode) -> int:
        def dfs(node: TreeNode | None, limit: int) -> int:
            if not node:
                return 0

            new_limit = max(limit, node.val)
            left = dfs(node.left, new_limit)
            right = dfs(node.right, new_limit)
            return (node.val >= limit) + left + right

        return dfs(head, head.val)
