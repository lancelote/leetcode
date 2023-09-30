from collections import Counter


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        steps = 0
        count = Counter(nums)

        for v in count.values():
            if v == 1:
                return -1
            elif v % 3 == 0:
                steps += v // 3
            elif v % 3 == 1:
                v -= 4
                steps += 2
                steps += v // 3
            elif v % 3 == 2:
                steps += v // 3 + 1
            else:
                raise ValueError

        return steps
