import copy


class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result: list[list[int]] = []

        def dfs(x: int, total: int, so_far: list[int]) -> None:
            if len(so_far) > k:
                return

            if total == n and len(so_far) == k:
                result.append(copy.copy(so_far))
                return

            if total > n:
                return

            if x > 9:
                return

            so_far.append(x)
            total += x
            dfs(x + 1, total, so_far)
            total -= x
            so_far.pop()

            dfs(x + 1, total, so_far)

        dfs(1, 0, [])
        return result
