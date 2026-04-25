from src.utils.binary_tree import TreeNode


class Solution:
    def dfs(self, root: TreeNode | None, parent: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val if parent.left is root else 0

        return self.dfs(root.left, root) + self.dfs(root.right, root)

    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        return self.dfs(root.left, root) + self.dfs(root.right, root)
