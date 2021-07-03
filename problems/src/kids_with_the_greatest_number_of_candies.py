from typing import List


class Solution:
    def kidsWithCandies(self, kids: List[int], extra: int) -> List[bool]:
        smallest_to_pass = max(kids) - extra
        return [kid >= smallest_to_pass for kid in kids]
