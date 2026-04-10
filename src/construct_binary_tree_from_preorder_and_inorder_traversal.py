from src.utils.binary_tree import TreeNode


class Solution:
    def buildTree(
        self, preorder: list[int], inorder: list[int]
    ) -> TreeNode | None:
        to_inorder_i = {x: i for i, x in enumerate(inorder)}
        preorder_i = 0

        def dfs(left: int, right: int) -> TreeNode | None:
            nonlocal preorder_i

            if left > right:
                return None

            val = preorder[preorder_i]
            inorder_i = to_inorder_i[val]
            node = TreeNode(val)

            preorder_i += 1

            node.left = dfs(left, inorder_i - 1)
            node.right = dfs(inorder_i + 1, right)

            return node

        return dfs(0, len(inorder) - 1)
