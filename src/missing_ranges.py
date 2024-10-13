class Solution:
    def findMissingRanges(
        self, nums: list[int], lower: int, upper: int
    ) -> list[list[int]]:
        if not nums:
            return [[lower, upper]]

        result: list[list[int]] = []
        left = lower

        for num in nums:
            if num == left:
                left += 1
            elif num > left:
                result.append([left, num - 1])
                left = num + 1

        if left <= upper:
            result.append([left, upper])

        return result
