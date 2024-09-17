class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        result: list[str] = []
        left = right = nums[0]

        def append() -> None:
            if left == right:
                result.append(f"{left}")
            else:
                result.append(f"{left}->{right}")

        for i in range(1, len(nums)):
            if nums[i] == right + 1:
                right = nums[i]
            else:
                append()
                left = right = nums[i]

        append()
        return result
