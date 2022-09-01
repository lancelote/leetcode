from src.utils.binary_tree import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        def dfs(node: TreeNode | None, limit: int) -> None:
            nonlocal good

            if not node:
                return

            if node.val >= limit:
                good += 1

            dfs(node.left, max(node.val, limit))
            dfs(node.right, max(node.val, limit))

        dfs(root, root.val)
        return good
