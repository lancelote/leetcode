class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        assert prices

        hold = -prices[0]
        free = 0

        for i in range(1, len(prices)):
            new_hold = max(hold, free - prices[i])
            new_free = max(free, hold + prices[i] - fee)

            hold = new_hold
            free = new_free

        return max(hold, free)
