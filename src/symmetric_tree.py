from src.utils.binary_tree import TreeNode


def dfs(left: TreeNode | None, right: TreeNode | None) -> bool:
    if not left and not right:
        return True
    elif not left or not right or left.val != right.val:
        return False
    else:
        return dfs(left.left, right.right) and dfs(left.right, right.left)


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        return dfs(root.left, root.right)
