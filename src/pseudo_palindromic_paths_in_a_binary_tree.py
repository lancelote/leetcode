from src.utils.binary_tree import TreeNode


class Solution:
    def is_pseudo_palindromic(self, counter: list[int]) -> bool:
        odd_count = 0

        for x in counter:
            if x % 2 == 1:
                odd_count += 1
                if odd_count > 1:
                    return False

        return True

    def pseudoPalindromicPaths(self, root: TreeNode | None) -> int:
        result = 0
        counter: list[int] = [0] * 9

        def dfs(node: TreeNode | None) -> None:
            nonlocal result

            if node is None:
                return

            counter[node.val - 1] += 1

            if node.left is None and node.right is None:
                result += self.is_pseudo_palindromic(counter)

            dfs(node.left)
            dfs(node.right)

            counter[node.val - 1] -= 1

        dfs(root)
        return result
