from typing import List


class Solution:
    def restoreString(self, text: str, indexes: List[int]) -> str:
        return "".join(letter for (_, letter) in sorted(zip(indexes, text)))
