class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        max_count = 0

        for x in nums:
            if x == 1:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 0

        return max(count, max_count)
