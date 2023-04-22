class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result: list[str] = []

        for a, b in zip(word1, word2):
            result.append(a)
            result.append(b)

        n = len(result) // 2

        for i in range(n, len(word1)):
            result.append(word1[i])

        for i in range(n, len(word2)):
            result.append(word2[i])

        return "".join(result)
