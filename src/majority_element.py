class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        result = nums[0]
        count = 0

        for num in nums:
            if num == result:
                count += 1
            elif count == 1:
                result = num
            else:
                count -= 1

        return result
