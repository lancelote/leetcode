from functools import cache


class Solution:
    def canFinish(
        self, num_courses: int, prerequisites: list[list[int]]
    ) -> bool:
        graph: list[list[int]] = [[] for _ in range(num_courses)]

        for u, v in prerequisites:
            graph[u].append(v)

        seen: set[int] = set()

        @cache
        def has_cycle(node: int) -> bool:
            if node in seen:
                return True

            seen.add(node)

            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True

            seen.remove(node)
            return False

        for x in range(num_courses):
            if has_cycle(x):
                return False

        return True
