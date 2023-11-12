from collections import defaultdict
from collections import deque


class Solution:
    def numBusesToDestination(
        self, routes: list[list[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0

        stop_to_buses: dict[int, list[int]] = defaultdict(list)

        for bus, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus)

        visited: set[int] = set()
        to_visit: deque[tuple[int, int]] = deque()

        for bus in stop_to_buses[source]:
            visited.add(bus)

            for stop in routes[bus]:
                to_visit.append((1, stop))

        while to_visit:
            path, stop = to_visit.popleft()
            buses = stop_to_buses[stop]

            if stop == target:
                return path

            for bus in buses:
                if bus in visited:
                    continue

                visited.add(bus)
                for stop in routes[bus]:
                    to_visit.append((path + 1, stop))

        return -1
