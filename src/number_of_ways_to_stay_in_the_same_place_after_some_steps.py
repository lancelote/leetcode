from functools import cache

MOD = 10**9 + 7


class Solution:
    def numWays(self, steps: int, arr_len: int) -> int:
        @cache
        def dfs(pos: int, steps_left: int) -> int:
            if pos < 0 or pos >= arr_len:
                return 0

            if steps_left == 0:
                return 1 if pos == 0 else 0

            return sum(
                (
                    dfs(pos - 1, steps_left - 1),
                    dfs(pos, steps_left - 1),
                    dfs(pos + 1, steps_left - 1),
                )
            )

        return dfs(0, steps) % MOD
