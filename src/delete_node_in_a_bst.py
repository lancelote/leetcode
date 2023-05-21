from src.utils.binary_tree import TreeNode


class Solution:
    def search_min(self, root: TreeNode) -> int:
        while root.left:
            root = root.left
        return root.val

    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                return root.left
            else:
                min_val = self.search_min(root.right)
                root.val = min_val
                root.right = self.deleteNode(root.right, min_val)

        return root
