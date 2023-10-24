from src.utils.binary_tree import TreeNode


class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        largest: list[int] = []

        def dfs(level: int, node: TreeNode | None) -> None:
            if node is None:
                return

            if len(largest) < level + 1:
                largest.append(node.val)
            else:
                largest[level] = max(largest[level], node.val)

            dfs(level + 1, node.left)
            dfs(level + 1, node.right)

        dfs(0, root)
        return largest
