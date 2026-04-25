class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        result = prices[::]
        stack: list[int] = []

        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                last_idx = stack.pop()
                result[last_idx] = prices[last_idx] - prices[i]
            stack.append(i)

        return result
