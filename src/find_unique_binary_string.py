class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        assert nums

        n = len(nums[0])
        ints = {int(x, base=2) for x in nums}

        for x in range(2**n):
            if x not in ints:
                return bin(x)[2:].rjust(n, "0")

        raise ValueError("no unique strings")
