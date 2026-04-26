class Solution:
    def binary_search(self, q: int, pre_sum: list[int]) -> int:
        left, right = 0, len(pre_sum) - 1
        while left <= right:
            middle = left + (right - left) // 2

            if pre_sum[middle] == q:
                return middle + 1

            if pre_sum[middle] > q:
                right = middle - 1
            else:
                left = middle + 1

        return left

    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        pre_sum = [0] * len(nums)

        running_sum = 0
        for i, x in enumerate(sorted(nums)):
            running_sum += x
            pre_sum[i] = running_sum

        return [self.binary_search(q, pre_sum) for q in queries]
