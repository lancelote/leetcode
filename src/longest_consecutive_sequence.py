class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        unique_nums = set(nums)
        longest_sequence = 0

        for num in nums:
            is_start_of_sequence = num - 1 not in unique_nums
            if is_start_of_sequence:
                current_length = 0
                while num + current_length in unique_nums:
                    current_length += 1
                longest_sequence = max(longest_sequence, current_length)

        return longest_sequence
