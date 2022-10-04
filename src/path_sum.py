from src.utils.binary_tree import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode | None, target_sum: int) -> bool:
        def dfs(node: TreeNode | None, current_sum: int) -> bool:
            if not node:
                return False

            current_sum += node.val

            if not node.left and not node.right:
                return current_sum == target_sum

            return dfs(node.left, current_sum) or dfs(node.right, current_sum)

        return dfs(root, 0)
