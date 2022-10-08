from collections import defaultdict


class Solution:
    def valid_tree(self, n: int, edges: list[list[int]]) -> bool:
        seen: set[int] = set()
        children: dict[int, list[int]] = defaultdict(list)

        for x, y in edges:
            children[x].append(y)
            children[y].append(x)

        def dfs(node: int, prev: int) -> bool:
            if node in seen:
                return False

            seen.add(node)

            for child in children[node]:
                if child == prev:
                    continue
                if not dfs(child, node):
                    return False

            return True

        return dfs(0, 0) and len(seen) == n
