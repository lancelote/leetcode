class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        dp = [0] * k
        result = [0] * k

        for i in range(n):
            new_dp = [0] * k

            r = nums[i] % k
            new_dp[r] += 1

            for r in range(k):
                new_dp[(r * nums[i]) % k] += dp[r]

            dp = new_dp

            for r in range(k):
                result[r] += dp[r]

        return result
