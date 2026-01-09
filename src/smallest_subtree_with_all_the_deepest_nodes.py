from src.utils.binary_tree import TreeNode


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode | None) -> TreeNode | None:
        def dfs(
            depth: int, node: TreeNode | None
        ) -> tuple[int, TreeNode | None]:
            if not node:
                return -1, None

            ld, lnode = dfs(depth + 1, node.left)
            rd, rnode = dfs(depth + 1, node.right)

            if lnode and rnode and ld == rd:
                return ld, node

            if lnode and ld > rd:
                return ld, lnode

            if rnode and rd > ld:
                return rd, rnode

            return depth, node

        _, result = dfs(0, root)
        return result
