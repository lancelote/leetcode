from src.utils.binary_tree import TreeNode


class Solution:
    def averageOfSubtree(self, root: TreeNode | None) -> int:
        count = 0

        def dfs(node: TreeNode | None) -> tuple[int, int]:
            nonlocal count

            if node is None:
                return 0, 0

            left_count, left_total = dfs(node.left)
            right_count, right_total = dfs(node.right)

            local_count = 1 + left_count + right_count
            local_total = node.val + left_total + right_total

            if int(local_total / local_count) == node.val:
                count += 1

            return local_count, local_total

        dfs(root)
        return count
