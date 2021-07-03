from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]

        for encoded_item in encoded:
            decoded = encoded_item ^ first
            first = decoded
            result.append(decoded)

        return result
