from src.utils.binary_tree import TreeNode


class Solution:
    def tree2str(self, root: TreeNode | None) -> str:
        result: list[str] = []

        def dfs(node: TreeNode) -> None:
            result.append(str(node.val))

            if node.left:
                result.append("(")
                dfs(node.left)
                result.append(")")
            if node.right:
                if node.left is None:
                    result.append("()")
                result.append("(")
                dfs(node.right)
                result.append(")")

        dfs(root)
        return "".join(result)
