from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        values = Counter(arr).values()
        return len(set(values)) == len(values)
