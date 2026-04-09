from src.utils.binary_tree import TreeNode


def dfs(node1: TreeNode | None, node2: TreeNode | None) -> bool:
    if node1 is None and node2 is None:
        return True

    if node1 is None or node2 is None:
        return False

    if node1.val != node2.val:
        return False

    return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        return dfs(root.left, root.right)
