from src.utils.binary_tree import TreeNode


class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        return root
