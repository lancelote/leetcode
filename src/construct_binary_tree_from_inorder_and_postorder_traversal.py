from src.utils.binary_tree import TreeNode


class Solution:
    def buildTree(
        self, inorder: list[int], postorder: list[int]
    ) -> TreeNode | None:
        val_to_in_idx = {x: i for i, x in enumerate(inorder)}

        def dfs(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None

            val = postorder.pop()
            in_idx = val_to_in_idx[val]

            node = TreeNode(val)
            node.right = dfs(in_idx + 1, right)
            node.left = dfs(left, in_idx - 1)

            return node

        return dfs(0, len(inorder) - 1)
