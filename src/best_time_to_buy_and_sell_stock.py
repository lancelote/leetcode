class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 0
        max_profit = 0

        while right < len(prices):
            current_profit = prices[right] - prices[left]
            max_profit = max(max_profit, current_profit)
            if current_profit < 0:
                left = right
            right += 1

        return max_profit
