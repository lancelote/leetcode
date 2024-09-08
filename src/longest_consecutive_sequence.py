class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums:
            current_len = 1

            if (num - 1) in nums_set:
                continue  # not a start of a sequence

            while (num + 1) in nums_set:
                current_len += 1
                num += 1

            longest = max(longest, current_len)

        return longest
