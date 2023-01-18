class Solution:
    def restoreString(self, text: str, indexes: list[int]) -> str:
        return "".join(letter for (_, letter) in sorted(zip(indexes, text)))
