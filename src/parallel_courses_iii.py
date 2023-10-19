from collections import defaultdict


class Solution:
    def minimumTime(
        self, n: int, relations: list[list[int]], time: list[int]
    ) -> int:
        start_to_end = defaultdict(list)
        for start, end in relations:
            start_to_end[start].append(end)

        dp = [0] * (n + 1)

        def dfs(node: int) -> int:
            if dp[node]:
                return dp[node]

            dp[node] = time[node - 1]
            if start_to_end[node]:
                dp[node] += max(dfs(nb) for nb in start_to_end[node])
            return dp[node]

        for i in range(1, n + 1):
            dfs(i)

        return max(dp)
