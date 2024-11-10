from src.utils.binary_tree import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode | None, target_sum: int) -> bool:
        def dfs(node: TreeNode | None, total: int = 0) -> bool:
            if not node:
                return False

            total += node.val

            if not node.left and not node.right:
                return total == target_sum

            return dfs(node.left, total) or dfs(node.right, total)

        return dfs(root)
