from src.utils.binary_tree import TreeNode


class Solution:
    def rob(self, root: TreeNode | None) -> int:
        def dfs(node: TreeNode | None) -> tuple[int, int]:
            if node is None:
                return 0, 0

            left = dfs(node.left)
            right = dfs(node.right)

            return (
                node.val + left[1] + right[1],
                max(left) + max(right),
            )

        return max(dfs(root))
