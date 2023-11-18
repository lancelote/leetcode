class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        assert nums

        n = len(nums)
        nums = sorted(nums)

        left = right = 0
        total = 0
        max_size = 0

        while right < n:
            total += nums[right]

            while right < n and nums[right] * (right - left + 1) > total + k:
                total -= nums[left]
                left += 1

            max_size = max(max_size, right - left + 1)
            right += 1

        return max_size
