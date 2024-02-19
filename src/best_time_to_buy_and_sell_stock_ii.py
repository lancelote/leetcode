class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        assert prices

        n = len(prices)
        total_profit = 0
        last = prices[-1]

        for i in range(n - 1, -1, -1):
            if prices[i] < last:
                total_profit += last - prices[i]
            last = prices[i]

        return total_profit
