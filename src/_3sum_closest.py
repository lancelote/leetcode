import sys


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        sorted_nums = sorted(nums)
        smallest_diff = sys.maxsize

        for start in range(0, len(sorted_nums) - 2):
            left = start + 1
            right = len(sorted_nums) - 1

            while left < right:
                current_sum = (
                    sorted_nums[start] + sorted_nums[left] + sorted_nums[right]
                )

                if abs(target - current_sum) < abs(smallest_diff):
                    smallest_diff = target - current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum

        return target - smallest_diff
