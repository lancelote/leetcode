class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        cache: dict[tuple[int, int, int], int] = {}

        def dfs(i: int, left: int, right: int) -> int:
            if i == len(stones):
                return abs(left - right)
            if (i, left, right) in cache:
                return cache[(i, left, right)]
            cache[(i, left, right)] = min(
                dfs(i + 1, left + stones[i], right),
                dfs(i + 1, left, right + stones[i]),
            )
            return cache[(i, left, right)]

        return dfs(0, 0, 0)
