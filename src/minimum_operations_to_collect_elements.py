class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        expected = {i for i in range(1, k + 1)}
        steps = 0

        while expected:
            x = nums.pop()
            if x in expected:
                expected.remove(x)
            steps += 1

        return steps
