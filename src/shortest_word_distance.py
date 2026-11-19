import sys


class Solution:
    def shortestDistance(
        self, words_dict: list[str], word1: str, word2: str
    ) -> int:
        current = ""
        dist = 0
        result = sys.maxsize

        for word in words_dict:
            if word == word1 or word == word2:
                if current != "" and word != current:
                    result = min(result, dist)
                current = word
                dist = 0
            dist += 1

        return result
