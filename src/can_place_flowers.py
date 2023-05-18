class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        i = 0

        while i < len(flowerbed):
            if n == 0:
                return True
            if flowerbed[i] == 1:
                i += 1
            elif (
                i < 2
                and (i + 1 < len(flowerbed) - 1 and flowerbed[i + 1] == 0)
                or i > len(flowerbed) - 2
                or flowerbed[i + 1] == 0
            ):
                n -= 1
                i += 1
            i += 1

        return n == 0
