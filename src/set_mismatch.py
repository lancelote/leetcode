class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        wrong = 0
        expected = set(range(1, len(nums) + 1))

        for x in nums:
            try:
                expected.remove(x)
            except KeyError:
                wrong = x

        missing = expected.pop()
        return [wrong, missing]
