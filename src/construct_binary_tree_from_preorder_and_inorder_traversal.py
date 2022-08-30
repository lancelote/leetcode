from src.utils.binary_tree import TreeNode


class Solution:
    def buildTree(
        self, preorder: list[int], inorder: list[int]
    ) -> TreeNode | None:
        if not preorder or not inorder:
            return None

        preorder_iter = iter(preorder)

        def get_node(start: int, stop: int) -> TreeNode | None:
            if start == stop:
                return None
            root = TreeNode(next(preorder_iter))
            root_idx = inorder.index(root.val)

            root.left = get_node(start, root_idx)
            root.right = get_node(root_idx + 1, stop)

            return root

        return get_node(0, len(preorder))
