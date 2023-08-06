from collections import defaultdict


class Solution:
    def minimumSeconds(self, nums: list[int]) -> int:
        n = len(nums)
        indexes: dict[int, list[int]] = defaultdict(list)

        for i, x in enumerate(nums):
            indexes[x].append(i)

        answer = n // 2

        for values in indexes.values():
            longest = 0

            for i in range(len(values) - 1):
                distance = (values[i + 1] - values[i]) // 2
                longest = max(longest, distance)

            distance = (n - values[-1] + values[0]) // 2
            longest = max(longest, distance)

            answer = min(answer, longest)

        return answer
