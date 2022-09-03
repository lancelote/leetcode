class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        sums = set()

        for i in range(0, len(nums) - 1):
            new_sum = nums[i] + nums[i + 1]
            if new_sum in sums:
                return True
            sums.add(new_sum)

        return False
