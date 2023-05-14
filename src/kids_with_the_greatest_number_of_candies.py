class Solution:
    def kidsWithCandies(self, kids: list[int], extra: int) -> list[bool]:
        diff_to_pass = max(kids) - extra
        return [kid >= diff_to_pass for kid in kids]
