class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        unique_nums = set(nums)
        sequence_starts: list[int] = []

        for num in nums:
            if num - 1 not in unique_nums:
                sequence_starts.append(num)

        longest_sequence = 0
        for sequence_start in sequence_starts:
            current_sequence_length = 0
            item = sequence_start
            while item in unique_nums:
                current_sequence_length += 1
                item += 1
            longest_sequence = max(longest_sequence, current_sequence_length)

        return longest_sequence
