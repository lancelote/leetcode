from src.utils.binary_tree import TreeNode


class Solution:
    def find_min(self, node: TreeNode) -> int:
        assert node.right

        node = node.right

        while node.left:
            node = node.left

        return node.val

    def find_max(self, node: TreeNode) -> int:
        assert node.left

        node = node.left

        while node.right:
            node = node.right

        return node.val

    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root:
            return None
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return None
            elif root.right:
                root.val = self.find_min(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.find_max(root)
                root.left = self.deleteNode(root.left, root.val)

        return root
