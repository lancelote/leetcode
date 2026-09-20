class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest_sequence = 0
        unique_elements = set(nums)

        for num in unique_elements:
            if num - 1 not in unique_elements:
                current_num = num
                current_sequence = 1

                while current_num + 1 in unique_elements:
                    current_num += 1
                    current_sequence += 1

                longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence
