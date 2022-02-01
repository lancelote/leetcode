class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        assert prices

        profit = 0
        left, right = 0, 1

        while right < len(prices):
            diff = prices[right] - prices[left]

            if diff < 0:
                left = right
            elif diff > profit:
                profit = diff
            right += 1

        return profit
