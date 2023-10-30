def number_of_ones(num: int) -> int:
    return bin(num)[2:].count("1")


class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        return sorted(arr, key=lambda x: (number_of_ones(x), x))
