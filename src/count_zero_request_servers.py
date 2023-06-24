from collections import Counter


class Solution:
    def countServers(
        self, n: int, logs: list[list[int]], x: int, queries: list[int]
    ) -> list[int]:
        result = [0] * len(queries)
        right, left = 0, 0

        requests: dict[int, int] = Counter()
        unique_servers = 0

        logs = sorted(logs, key=lambda log: log[1])

        for query_time, query_id in sorted(
            (query_time, query_id)
            for query_id, query_time in enumerate(queries)
        ):
            while right < len(logs) and logs[right][1] <= query_time:
                requests[logs[right][0]] += 1
                unique_servers += requests[logs[right][0]] == 1
                right += 1
            while left < right and logs[left][1] < query_time - x:
                requests[logs[left][0]] -= 1
                unique_servers -= requests[logs[left][0]] == 0
                left += 1
            result[query_id] = n - unique_servers

        return result
