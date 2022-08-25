import typing
from collections import defaultdict


class Solution:
    def canConstruct(self, ransom_note: str, magazine: str) -> bool:
        char_counter: typing.DefaultDict[str, int] = defaultdict(int)

        for char in magazine:
            char_counter[char] += 1

        for char in ransom_note:
            if char_counter[char] == 0:
                return False
            char_counter[char] -= 1
        return True
