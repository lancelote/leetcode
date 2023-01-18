class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        return sum(len(str(num)) % 2 == 0 for num in nums)
