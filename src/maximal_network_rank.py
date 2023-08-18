from collections import defaultdict


class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        cities: dict[int, set[int]] = defaultdict(set)

        for a, b in roads:
            cities[a].add(b)
            cities[b].add(a)

        max_network_rank = 0

        for i in range(n):
            for j in range(i + 1, n):
                network_rank = len(cities[i]) + len(cities[j])

                if j in cities[i]:
                    network_rank -= 1

                max_network_rank = max(max_network_rank, network_rank)

        return max_network_rank
