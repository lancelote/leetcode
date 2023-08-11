class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            new_dp = [0] * (amount + 1)
            new_dp[0] = 1

            for i in range(1, amount + 1):
                new_dp[i] = dp[i]

                if i - coin >= 0:
                    new_dp[i] += new_dp[i - coin]

            dp = new_dp

        return dp[-1]
