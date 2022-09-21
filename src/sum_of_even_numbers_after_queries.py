class Solution:
    def sumEvenAfterQueries(
        self, nums: list[int], queries: list[list[int]]
    ) -> list[int]:
        sum_even = sum(x for x in nums if x % 2 == 0)
        result = []

        for val, i in queries:
            if nums[i] % 2 == 0:
                if val % 2 == 0:
                    sum_even += val
                else:
                    sum_even -= nums[i]
            else:
                if val % 2 == 0:
                    pass
                else:
                    sum_even += nums[i] + val

            nums[i] += val
            result.append(sum_even)

        return result
