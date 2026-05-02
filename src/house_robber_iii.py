from src.utils.binary_tree import TreeNode


class Solution:
    def rob(self, root: TreeNode | None) -> int:
        def dfs(node: TreeNode | None, can_rob: bool) -> int:
            if not node:
                return 0

            if can_rob:
                return max(
                    node.val + dfs(node.left, False) + dfs(node.right, False),
                    dfs(node.left, True) + dfs(node.right, True),
                )
            else:
                return dfs(node.left, True) + dfs(node.right, True)

        return dfs(root, True)
