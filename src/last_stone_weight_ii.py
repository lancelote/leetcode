class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        total = sum(stones)
        half = total // 2
        cache: dict[tuple[int, int], int] = {}

        def dfs(i: int, pile: int) -> int:
            if i == len(stones) or pile >= half:
                return abs(pile - (total - pile))
            if (i, pile) in cache:
                return cache[(i, pile)]

            cache[(i, pile)] = min(
                dfs(i + 1, pile), dfs(i + 1, pile + stones[i])
            )

            return cache[(i, pile)]

        return dfs(0, 0)
