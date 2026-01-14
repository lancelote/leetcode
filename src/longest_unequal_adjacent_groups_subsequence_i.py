class Solution:
    def getWordsInLongestSubsequence(
        self, _: int, words: list[str], groups: list[int]
    ) -> list[str]:
        result: list[int] = []

        for i, group in enumerate(groups):
            if not result or groups[result[-1]] != group:
                result.append(i)

        return [words[i] for i in result]
