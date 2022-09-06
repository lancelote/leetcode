from src.utils.binary_tree import TreeNode


class Solution:
    def pruneTree(self, root: TreeNode | None) -> TreeNode | None:
        def dfs(node: TreeNode | None) -> bool:
            if node is None:
                return False

            left_has_1 = dfs(node.left)
            right_has_1 = dfs(node.right)

            if not left_has_1:
                node.left = None
            if not right_has_1:
                node.right = None

            return node.val == 1 or left_has_1 or right_has_1

        if not dfs(root):
            return None
        return root
