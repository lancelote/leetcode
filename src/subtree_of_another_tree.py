from src.utils.binary_tree import TreeNode


def same(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    if not root1 and not root2:
        return True
    if root1 and root2 and root1.val == root2.val:
        return same(root1.left, root2.left) and same(root1.right, root2.right)
    return False


class Solution:
    def isSubtree(
        self, root: TreeNode | None, sub_root: TreeNode | None
    ) -> bool:
        if not sub_root:
            return True
        if not root:
            return False
        if same(root, sub_root):
            return True

        return self.isSubtree(root.left, sub_root) or self.isSubtree(
            root.right, sub_root
        )
