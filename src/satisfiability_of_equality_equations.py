import re
from collections import defaultdict


class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        equal_graph: dict[str, list[str]] = defaultdict(list)
        not_equal: list[tuple[str, str, str]] = []

        def find(start: str, target: str) -> bool:
            visited: set[str] = set()
            to_visit: list[str] = [start]

            while to_visit:
                node = to_visit.pop()
                if node in visited:
                    continue
                if node == target:
                    return True
                visited.add(node)
                to_visit.extend(equal_graph[node])

            return False

        for eq in equations:
            match = re.match(r"(\w)(==|!=)(\w)", eq)
            assert match

            var1, op, var2 = match.groups()

            if op == "!=":
                not_equal.append((var1, op, var2))
            elif op == "==":
                equal_graph[var1].append(var2)
                equal_graph[var2].append(var1)

        for var1, _, var2 in not_equal:
            if find(var1, var2):
                return False

        return True
