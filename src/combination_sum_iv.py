class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = {0: 1}

        for curr_target in range(1, target + 1):
            dp[curr_target] = 0
            for num in nums:
                dp[curr_target] += dp.get(curr_target - num, 0)

        return dp[target]
