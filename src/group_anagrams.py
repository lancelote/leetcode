from collections import defaultdict
from collections.abc import Iterable


def count(phrase: str) -> tuple[int, ...]:
    counts: list[int] = [0] * 26
    for char in phrase:
        counts[ord(char) - ord("a")] += 1
    return tuple(counts)


class Solution:
    def groupAnagrams(self, strs: list[str]) -> Iterable[list[str]]:
        groups: dict[tuple[int, ...], list[str]] = defaultdict(list)

        for phrase in strs:
            groups[count(phrase)].append(phrase)

        return groups.values()
