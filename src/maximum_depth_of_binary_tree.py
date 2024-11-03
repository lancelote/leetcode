from src.utils.binary_tree import TreeNode


def dfs(node: TreeNode | None, depth: int = 0) -> int:
    if node is None:
        return depth

    left = dfs(node.left, depth + 1)
    right = dfs(node.right, depth + 1)

    return max(left, right)


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        return dfs(root)
