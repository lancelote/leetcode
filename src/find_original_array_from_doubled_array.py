from collections import Counter


class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        result: list[int] = []
        counter = Counter(changed)

        for x in sorted(changed):
            if counter[x] == 0:
                continue

            counter[x] -= 1
            counter[x * 2] -= 1

            if counter[x * 2] < 0:
                return []

            result.append(x)

        return result
