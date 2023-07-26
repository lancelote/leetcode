from src.utils.binary_tree import TreeNode


class Solution:
    def pathSum(self, root: TreeNode | None, target_sum: int) -> int:
        result = 0
        cache = {0: 1}

        def dfs(head: TreeNode | None, path: int) -> None:
            nonlocal result

            if head is None:
                return

            path += head.val
            result += cache.get(path - target_sum, 0)
            cache[path] = cache.get(path, 0) + 1

            dfs(head.left, path)
            dfs(head.right, path)

            cache[path] -= 1

        dfs(root, 0)
        return result
