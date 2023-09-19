class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        s1 = s2 = f0 = nums[0]

        while True:
            s1 = nums[s1]
            f0 = nums[f0]
            f0 = nums[f0]

            if s1 == f0:
                break

        while s1 != s2:
            s1 = nums[s1]
            s2 = nums[s2]

        return s1
