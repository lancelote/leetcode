from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        result: list[str] = []
        counter = Counter(s)

        for char, count in counter.most_common():
            result.append(char * count)

        return "".join(result)
