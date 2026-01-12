from src.utils.binary_tree import TreeNode


class Solution:
    def buildTree(
        self, inorder: list[int], postorder: list[int]
    ) -> TreeNode | None:
        n = len(inorder)
        postorder_idx = n - 1

        def dfs(left: int, right: int) -> TreeNode | None:
            nonlocal postorder_idx

            if left > right:
                return None

            value = postorder[postorder_idx]
            inorder_idx = val_to_inorder_idx[value]
            node = TreeNode(value)

            postorder_idx -= 1

            node.right = dfs(inorder_idx + 1, right)
            node.left = dfs(left, inorder_idx - 1)

            return node

        val_to_inorder_idx = {val: i for i, val in enumerate(inorder)}

        return dfs(0, n - 1)
