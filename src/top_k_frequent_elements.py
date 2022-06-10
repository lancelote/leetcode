from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts: dict[int, int] = defaultdict(int)
        freq: list[list[int]] = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            counts[num] += 1

        for num, count in counts.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        raise ValueError("failed to find enough numbers")
