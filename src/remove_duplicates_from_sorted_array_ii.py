class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        j = 1
        k = 1

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                k -= 1
                if k < 0:
                    continue

            if not nums[i - 1] == nums[i]:
                k = 1

            nums[j] = nums[i]
            j += 1

        return j
