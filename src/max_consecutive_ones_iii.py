class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_count = 0
        left, right = 0, 0

        for x in nums:
            if x == 1:
                pass
            elif k:
                k -= 1
            else:
                while nums[left] != 0:
                    left += 1
                left += 1

            right += 1
            max_count = max(right - left, max_count)

        return max_count
