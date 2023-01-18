class Solution:
    def kidsWithCandies(self, kids: list[int], extra: int) -> list[bool]:
        smallest_to_pass = max(kids) - extra
        return [kid >= smallest_to_pass for kid in kids]
