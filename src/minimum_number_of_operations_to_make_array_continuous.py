class Solution:
    def minOperations(self, nums: list[int]) -> int:
        orig_n = len(nums)
        nums = sorted(set(nums))
        n = len(nums)

        longest = 0
        left, right = 0, 0

        while left < n:
            limit = nums[left] + orig_n - 1

            while right < n and nums[right] <= limit:
                right += 1

            longest = max(longest, right - left)
            left += 1

        return orig_n - longest
