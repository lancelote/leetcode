import heapq


class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        assert nums

        result = nums[0]
        heap = [(-nums[0], 0)]

        for i in range(1, len(nums)):
            while heap and i - heap[0][1] > k:
                heapq.heappop(heap)

            curr_max = max(nums[i], -heap[0][0] + nums[i])
            result = max(result, curr_max)

            heapq.heappush(heap, (-curr_max, i))

        return result
