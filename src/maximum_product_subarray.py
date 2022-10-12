class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        result = max(nums)

        cur_max = 1
        cur_min = 1

        for x in nums:
            if x == 0:
                cur_max = 1
                cur_min = 1
                continue

            tmp = max(cur_max * x, cur_min * x, x)
            cur_min = min(cur_max * x, cur_min * x, x)
            cur_max = tmp

            result = max(result, cur_max, cur_min)

        return result
