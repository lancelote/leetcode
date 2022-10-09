from src.utils.binary_search_tree import TreeNode


class Solution:
    def findTarget(self, root: TreeNode | None, k: int) -> bool:
        seen: set[int] = set()

        def dfs(node: TreeNode | None) -> bool:
            if not node:
                return False
            if k - node.val in seen:
                return True
            seen.add(node.val)
            if dfs(node.left) or dfs(node.right):
                return True
            return False

        return dfs(root)
