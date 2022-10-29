from collections import defaultdict


def difference(word: str) -> tuple[int, ...]:
    result: list[int] = []

    for i in range(1, len(word)):
        result.append(ord(word[i]) - ord(word[i - 1]))

    return tuple(result)


class Solution:
    def oddString(self, words: list[str]) -> str:
        diffs: dict[tuple[int, ...], list[str]] = defaultdict(list)
        for word in words:
            diff = difference(word)
            diffs[diff].append(word)

        for _, v in diffs.items():
            if len(v) == 1:
                return v[0]

        raise ValueError
