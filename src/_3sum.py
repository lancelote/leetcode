class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        nums = sorted(nums)

        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue  # skip duplicate

            a = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                b = nums[left]
                c = nums[right]
                three_sum = a + b + c

                if three_sum == 0:
                    result.append([a, b, c])

                    left += 1
                    while left <= right and nums[left] == nums[left - 1]:
                        left += 1  # skip duplicates

                    right = len(nums) - 1
                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result
