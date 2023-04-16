class Solution:
    def leftRigthDifference(self, nums: list[int]) -> list[int]:
        result = []

        left_sum = 0
        right_sum = sum(nums)

        for num in nums:
            right_sum -= num

            result.append(abs(left_sum - right_sum))

            left_sum += num

        return result
