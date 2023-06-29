class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        highest = current = 0

        for x in gain:
            current += x
            highest = max(highest, current)

        return highest
