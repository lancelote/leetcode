from collections import defaultdict


class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        out_paths: dict[int, list[int]] = defaultdict(list)
        in_paths: dict[int, list[int]] = defaultdict(list)

        visited: set[int] = set()

        for a, b in connections:
            out_paths[a].append(b)
            in_paths[b].append(a)

        def dfs(city: int) -> int:
            visited.add(city)

            count = 0

            for next_city in in_paths[city]:
                if next_city not in visited:
                    count += dfs(next_city)

            for next_city in out_paths[city]:
                if next_city not in visited:
                    count += 1 + dfs(next_city)

            return count

        return dfs(0)
