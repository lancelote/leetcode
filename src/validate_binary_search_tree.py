from src.utils.binary_search_tree import TreeNode


def is_valid_dfs(root: TreeNode | None, low: int, high: int) -> bool:
    if not root:
        return True
    return (
        low < root.val < high
        and is_valid_dfs(root.left, low, root.val)
        and is_valid_dfs(root.right, root.val, high)
    )


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        return is_valid_dfs(root, -(2**31) - 1, 2**31)
