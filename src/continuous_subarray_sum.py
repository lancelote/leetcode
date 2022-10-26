class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainders = {0: -1}
        current_sum = 0

        for i, x in enumerate(nums):
            current_sum += x
            remainder = current_sum % k

            if remainder not in remainders:
                remainders[remainder] = i
            elif i - remainders[remainder] > 1:
                return True

        return False
