class NumArray:
    def __init__(self, nums: list[int]) -> None:
        n = len(nums)

        self.prefix: list[int] = [0] * n
        for i in range(n):
            self.prefix[i] = self.prefix[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]
