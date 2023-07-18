from src.utils.binary_tree import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def dfs(head: TreeNode | None, depth: int) -> int:
            if not head:
                return depth
            elif head.left and head.right:
                return max(
                    dfs(head.left, depth + 1), dfs(head.right, depth + 1)
                )
            elif head.left:
                return dfs(head.left, depth + 1)
            elif head.right:
                return dfs(head.right, depth + 1)
            else:
                return depth + 1

        return dfs(root, 0)
