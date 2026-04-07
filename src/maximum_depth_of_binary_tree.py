from src.utils.binary_tree import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
