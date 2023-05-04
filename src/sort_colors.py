class Solution:
    def sortColors(self, nums: list[int]) -> None:
        buckets = [0, 0, 0]

        for color in nums:
            buckets[color] += 1

        i = 0
        for color, count in enumerate(buckets):
            for _ in range(count):
                nums[i] = color
                i += 1
