class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        nums = sorted(nums, reverse=True)

        result = 0
        count = 0
        last = 0

        for x in nums:
            if x != last:
                result += count
            count += 1
            last = x

        return result
