from src.utils.binary_tree import TreeNode


class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        max_path = 0

        def dfs(node: TreeNode | None, path: int, go_left: bool) -> None:
            nonlocal max_path

            if not node:
                return

            max_path = max(max_path, path)

            if go_left:
                dfs(node.left, path + 1, False)
                dfs(node.right, 1, True)
            else:
                dfs(node.right, path + 1, True)
                dfs(node.left, 1, False)

        dfs(root, 0, False)
        dfs(root, 0, True)

        return max_path
