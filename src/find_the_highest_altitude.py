class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        current = largest = 0

        for dy in gain:
            current += dy

            if current > largest:
                largest = current

        return largest
