import sys
from functools import cache


class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        @cache
        def dfs(i: int, remain: int) -> int:
            if remain <= 0:
                return 0

            if i == len(cost):
                return sys.maxsize

            return min(
                cost[i] + dfs(i + 1, remain - 1 - time[i]),
                dfs(i + 1, remain),
            )

        return dfs(0, len(time))
