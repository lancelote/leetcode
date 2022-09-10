import sys


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        profit = [[0] * n for _ in range(k + 1)]

        for t in range(1, k + 1):
            max_tmp = -sys.maxsize

            for d in range(1, n):
                max_tmp = max(max_tmp, profit[t - 1][d - 1] - prices[d - 1])
                profit[t][d] = max(profit[t][d - 1], prices[d] + max_tmp)

        return profit[-1][-1]
