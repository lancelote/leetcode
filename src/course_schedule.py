from functools import cache


class Solution:
    def canFinish(self, _: int, prerequisites: list[list[int]]) -> bool:
        deps: dict[int, list[int]] = {}

        for [a, b] in prerequisites:
            if a not in deps:
                deps[a] = [b]
            else:
                deps[a].append(b)

        seen: set[int] = set()

        @cache
        def has_cycles(node: int) -> bool:
            if node in seen:
                return True

            seen.add(node)

            if node in deps:
                for x in deps[node]:
                    if has_cycles(x):
                        return True

            seen.remove(node)

            return False

        for k in deps.keys():
            if has_cycles(k):
                return False

        return True
