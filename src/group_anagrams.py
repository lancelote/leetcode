from collections import defaultdict


def get_count(word: str) -> tuple[int, ...]:
    counts = [0] * 26

    for letter in word:
        index = ord(letter) - ord("a")
        counts[index] += 1

    return tuple(counts)


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        count_to_words: dict[tuple[int, ...], list[str]] = defaultdict(list)

        for word in strs:
            count = get_count(word)
            count_to_words[count].append(word)

        return list(count_to_words.values())
