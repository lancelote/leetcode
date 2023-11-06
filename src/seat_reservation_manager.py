import heapq


class SeatManager:
    def __init__(self, n: int):
        self.i = 1
        self._unreserved: list[int] = []

    def reserve(self) -> int:
        if self._unreserved and self._unreserved[0] < self.i:
            result = heapq.heappop(self._unreserved)
        else:
            result = self.i
            self.i += 1

        return result

    def unreserve(self, seat_number: int) -> None:
        heapq.heappush(self._unreserved, seat_number)
