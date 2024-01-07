import heapq


class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        n = len(costs)

        left = costs[:candidates]
        right = costs[max(candidates, n - candidates) :]

        heapq.heapify(left)
        heapq.heapify(right)

        total = 0

        next_left = candidates
        next_right = n - 1 - candidates

        for _ in range(k):
            if not right or left and left[0] <= right[0]:
                total += heapq.heappop(left)

                if next_left <= next_right:
                    heapq.heappush(left, costs[next_left])
                    next_left += 1
            else:
                total += heapq.heappop(right)

                if next_left <= next_right:
                    heapq.heappush(right, costs[next_right])
                    next_right -= 1

        return total
