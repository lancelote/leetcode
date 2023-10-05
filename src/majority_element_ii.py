class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        third = len(nums) // 3
        h: dict[int, int] = {}

        for x in nums:
            h[x] = h.get(x, 0) + 1
            if len(h) > 2:
                for k in list(h.keys()):
                    h[k] -= 1
                    if h[k] == 0:
                        del h[k]

        return [k for k in h.keys() if nums.count(k) > third]
