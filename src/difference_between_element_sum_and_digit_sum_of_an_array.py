from collections.abc import Iterator


def digits(num: int) -> Iterator[int]:
    while num:
        yield num % 10
        num //= 10


class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        return abs(sum(nums) - sum(sum(digits(num)) for num in nums))
