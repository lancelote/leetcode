import heapq


class Solution:
    def maximumRobots(
        self, charge_times: list[int], running_costs: list[int], budget: int
    ) -> int:
        n = len(charge_times)
        max_consecutive = 0
        sum_running_costs = 0
        max_charge_times: list[tuple[int, int]] = []
        left = 0

        for right in range(n):
            sum_running_costs += running_costs[right]
            heapq.heappush(max_charge_times, (-charge_times[right], right))

            while (
                max_charge_times
                and (-max_charge_times[0][0])
                + (right - left + 1) * sum_running_costs
                > budget
            ):
                sum_running_costs -= running_costs[left]
                if max_charge_times[0][1] <= left:
                    heapq.heappop(max_charge_times)
                left += 1

            max_consecutive = max(max_consecutive, right - left + 1)

        return max_consecutive
