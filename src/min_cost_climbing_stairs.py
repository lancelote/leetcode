class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        a, b = cost[0], cost[1]

        for i in range(2, len(cost)):
            a, b = b, cost[i] + min(a, b)

        return min(a, b)
