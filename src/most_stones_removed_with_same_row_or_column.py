import typing
from collections import defaultdict


class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        visited: set[tuple[int, int]] = set()

        xs: typing.DefaultDict[int, list[int]] = defaultdict(list)
        ys: typing.DefaultDict[int, list[int]] = defaultdict(list)

        for x, y in stones:
            xs[x].append(y)
            ys[y].append(x)

        def dfs(x: int, y: int) -> None:
            if (x, y) not in visited:
                visited.add((x, y))

                for ny in xs[x]:
                    dfs(x, ny)

                for nx in ys[y]:
                    dfs(nx, y)

        connected = 0
        for x, y in stones:
            if (x, y) not in visited:
                dfs(x, y)
                connected += 1

        return len(stones) - connected
