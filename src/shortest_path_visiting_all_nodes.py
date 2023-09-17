from collections import deque


class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)

        masks = [1 << shift for shift in range(n)]
        all_visit = (1 << n) - 1
        queue = deque([(i, masks[i]) for i in range(n)])
        steps = 0

        visited_states = [{masks[i]} for i in range(n)]

        while queue:
            step_size = len(queue)

            for _ in range(step_size):
                node, visited = queue.popleft()

                if visited == all_visit:
                    return steps

                for neighbor in graph[node]:
                    new_visited = visited | masks[neighbor]

                    if new_visited == all_visit:
                        return steps + 1

                    if new_visited not in visited_states[neighbor]:
                        visited_states[neighbor].add(new_visited)
                        queue.append((neighbor, new_visited))

            steps += 1

        raise ValueError("path not found")
