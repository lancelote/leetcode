class Solution:
    def maxSubarrays(self, nums: list[int]) -> int:
        min_score = nums[0]
        for i in range(1, len(nums)):
            min_score &= nums[i]

        if min_score > 0:
            return 1

        result = 0
        score = 2**32 - 1

        for x in nums:
            score &= x

            if score == 0:
                result += 1
                score = 2**32 - 1

        return result
