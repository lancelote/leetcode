class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        result = [first]

        for encoded_item in encoded:
            decoded = encoded_item ^ first
            first = decoded
            result.append(decoded)

        return result
