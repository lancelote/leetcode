class Solution:
    def successfulPairs(
        self, spells: list[int], potions: list[int], success: int
    ) -> list[int]:
        potions.sort()
        result: list[int] = []

        for spell in spells:
            left, right = 0, len(potions) - 1
            idx = len(potions)

            while left <= right:
                middle = (left + right) // 2

                if spell * potions[middle] >= success:
                    right = middle - 1
                    idx = middle
                else:
                    left = middle + 1

            result.append(len(potions) - idx)

        return result
