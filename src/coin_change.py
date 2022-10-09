from collections import defaultdict


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp: dict[int, int] = defaultdict(lambda: amount + 1)
        dp[0] = 0

        for sub_amount in range(1, amount + 1):
            for coin in coins:
                diff = sub_amount - coin
                if diff >= 0:
                    dp[sub_amount] = min(dp[sub_amount], 1 + dp[diff])

        return dp[amount] if dp[amount] != amount + 1 else -1
