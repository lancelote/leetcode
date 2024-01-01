from collections import defaultdict
from collections import deque


class Solution:
    def calcEquation(
        self,
        equations: list[list[str]],
        values: list[float],
        queries: list[list[str]],
    ) -> list[float]:
        eqs = defaultdict(list)

        for i in range(len(equations)):
            a, b = equations[i]
            eqs[a].append((b, values[i]))
            eqs[b].append((a, 1 / values[i]))

        def bfs(src: str, target: str) -> float:
            if src not in eqs or target not in eqs:
                return -1

            d: deque[tuple[str, float]] = deque()
            visited = set()

            d.append((src, 1))
            visited.add(src)

            while d:
                c, w = d.popleft()

                if c == target:
                    return w

                for neighbor, val in eqs[c]:
                    if neighbor not in visited:
                        d.append((neighbor, w * val))
                        visited.add(neighbor)

            return -1

        return [bfs(a, b) for a, b in queries]
