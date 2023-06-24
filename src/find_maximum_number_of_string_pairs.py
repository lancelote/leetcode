class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        pairs = 0
        to_find: set[str] = set()

        for word in words:
            r_word = word[::-1]
            if r_word in to_find:
                pairs += 1
            else:
                to_find.add(word)

        return pairs
