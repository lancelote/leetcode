from src.utils.binary_tree import TreeNode


class Solution:
    def buildTree(
        self, preorder: list[int], inorder: list[int]
    ) -> TreeNode | None:
        root_pre_i = 0

        def dfs(left: int, right: int) -> TreeNode | None:
            nonlocal root_pre_i

            if left > right:
                return None

            value = preorder[root_pre_i]
            root_in_i = val_to_index[value]
            node = TreeNode(value)

            root_pre_i += 1

            node.left = dfs(left, root_in_i - 1)
            node.right = dfs(root_in_i + 1, right)

            return node

        val_to_index = {val: i for i, val in enumerate(inorder)}

        return dfs(0, len(preorder) - 1)
