class Solution:
    def maxScore(self, nums: list[int], x: int) -> int:
        eve = -x if nums[0] & 1 else 0 + nums[0]
        odd = 0 if nums[0] & 1 else -x + nums[0]

        for i in range(1, len(nums)):
            if nums[i] & 1:
                odd = nums[i] + max(odd, eve - x)
            else:
                eve = nums[i] + max(eve, odd - x)

        return max(eve, odd)
