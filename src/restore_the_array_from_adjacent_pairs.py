from collections import defaultdict
from collections import deque


class Solution:
    def restoreArray(self, adjacent_pairs: list[list[int]]) -> list[int]:
        n = len(adjacent_pairs) + 1
        connections = defaultdict(list)

        for [a, b] in adjacent_pairs:
            connections[a].append(b)
            connections[b].append(a)

        used: set[int] = set()
        result: deque[int] = deque()

        some = adjacent_pairs[0][0]

        used.add(some)
        result.append(some)

        def dfs() -> bool:
            if len(result) == n:
                return True

            for candidate in connections[result[0]]:
                if candidate not in used:
                    used.add(candidate)
                    result.appendleft(candidate)

                    if dfs():
                        return True

                    used.remove(candidate)
                    result.popleft()

            for candidate in connections[result[-1]]:
                if candidate not in used:
                    used.add(candidate)
                    result.append(candidate)

                    if dfs():
                        return True

                    used.remove(candidate)
                    result.popleft()

            return False

        dfs()
        return list(result)
