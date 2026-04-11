from src.utils.binary_tree import TreeNode


class Solution:
    def buildTree(
        self, inorder: list[int], postorder: list[int]
    ) -> TreeNode | None:
        post_idx = len(postorder) - 1
        val_to_in_idx = {x: i for i, x in enumerate(inorder)}

        def dfs(left: int, right: int) -> TreeNode | None:
            nonlocal post_idx

            if left > right:
                return None

            val = postorder[post_idx]
            in_idx = val_to_in_idx[val]

            post_idx -= 1

            node = TreeNode(val)
            node.right = dfs(in_idx + 1, right)
            node.left = dfs(left, in_idx - 1)

            return node

        return dfs(0, len(inorder) - 1)
