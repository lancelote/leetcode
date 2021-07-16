class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        total = 0

        for i, item in enumerate(arr):
            possible_start_indexes = i + 1
            possible_end_indexes = len(arr) - i
            times_contributed = possible_start_indexes * possible_end_indexes
            times_contributed_odd = (times_contributed + 1) // 2
            total += times_contributed_odd * item

        return total
