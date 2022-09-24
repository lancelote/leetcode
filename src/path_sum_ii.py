from src.utils.binary_tree import TreeNode


class Solution:
    def pathSum(
        self, root: TreeNode | None, target_sum: int
    ) -> list[list[int]]:
        result: list[list[int]] = []

        def dfs(node: TreeNode | None, path: list[int], total: int) -> None:
            if not node:
                return

            path.append(node.val)
            total += node.val

            if not node.left and not node.right:
                if total == target_sum:
                    result.append(list(path))
            else:
                dfs(node.left, path, total)
                dfs(node.right, path, total)

            path.pop()

        dfs(root, [], 0)
        return result
