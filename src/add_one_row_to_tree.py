from src.utils.binary_tree import TreeNode


class Solution:
    def addOneRow(
        self, root: TreeNode | None, val: int, depth: int
    ) -> TreeNode | None:
        def dfs(node: TreeNode | None, level: int) -> None:
            if not node:
                return

            if level == depth - 1:
                tmp_left = node.left
                tmp_right = node.right

                node.left = TreeNode(val, left=tmp_left)
                node.right = TreeNode(val, right=tmp_right)
                return

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dummy = TreeNode(left=root)
        dfs(dummy, 0)
        return dummy.left
