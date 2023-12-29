from src.utils.binary_tree import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        result: list[int] = []

        def dfs(node: TreeNode) -> None:
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            result.append(node.val)

        if root:
            dfs(root)
        return result
