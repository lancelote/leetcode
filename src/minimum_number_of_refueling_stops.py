import heapq


class Solution:
    def minRefuelStops(
        self, target: int, cur_fuel: int, stations: list[list[int]]
    ) -> int:
        fuel_pq: list[int] = []
        stops = 0
        i = 0

        while cur_fuel < target:
            # add all stations in reach
            while i < len(stations) and stations[i][0] <= cur_fuel:
                # use negative fuel to simulate maxheap
                heapq.heappush(fuel_pq, -stations[i][1])
                i += 1

            if not fuel_pq:
                return -1
            cur_fuel += -heapq.heappop(fuel_pq)
            stops += 1

        return stops
