def is_palindrome(word: str) -> bool:
    return word == word[::-1]


class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        result = []
        cache = {word: i for i, word in enumerate(words)}

        for word, i in cache.items():
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]

                if is_palindrome(prefix):
                    back = suffix[::-1]
                    if back != word and back in cache:
                        result.append([cache[back], i])

                if j != len(word) and is_palindrome(suffix):
                    back = prefix[::-1]
                    if back != word and back in cache:
                        result.append([i, cache[back]])

        return result
