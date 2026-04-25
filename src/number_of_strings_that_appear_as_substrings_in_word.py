class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        return sum(x in word for x in patterns)
