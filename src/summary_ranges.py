class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        ranges: list[str] = []

        a = nums[0]
        b = nums[0]

        def append_range() -> None:
            ranges.append(str(a) if a == b else f"{a}->{b}")

        for i in range(1, len(nums)):
            c = nums[i]

            if c - b == 1:
                b = c
            else:
                append_range()
                a = b = c

        append_range()
        return ranges
