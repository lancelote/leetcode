from collections import defaultdict


class Solution:
    def maxSum(self, nums: list[int], m: int, k: int) -> int:
        n = len(nums)

        current_sum = max_sum = 0

        counts: dict[int, int] = defaultdict(int)
        for i in range(k):
            current_sum += nums[i]
            counts[nums[i]] += 1

        if len(counts) >= m:
            max_sum = current_sum
        i = k

        while i < n:
            start = nums[i - k]
            end = nums[i]

            if counts[start] == 1:
                del counts[start]
            else:
                counts[start] -= 1
            counts[end] += 1

            current_sum += end - start
            if len(counts) >= m:
                max_sum = max(max_sum, current_sum)

            i += 1

        return max_sum
