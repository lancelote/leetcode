class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        days_set = set(days)
        dp = [0] * (days[-1] + 1)

        for day in range(1, days[-1] + 1):
            if day not in days_set:
                dp[day] = dp[day - 1] if day - 1 >= 0 else 0
            else:
                dp[day] = min(
                    costs[0] + (dp[day - 1] if day - 1 >= 0 else 0),
                    costs[1] + (dp[day - 7] if day - 7 >= 0 else 0),
                    costs[2] + (dp[day - 30] if day - 30 >= 0 else 0),
                )

        return dp[-1]
