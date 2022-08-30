from src.utils.binary_tree import TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        assert root

        max_path = root.val

        def dfs(node: TreeNode | None) -> int:
            nonlocal max_path

            if not node:
                return 0

            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))

            max_path = max(max_path, node.val + left_max + right_max)
            return node.val + max(left_max, right_max)

        dfs(root)
        return max_path
