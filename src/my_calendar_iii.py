class MyCalendarThree:
    def __init__(self):
        self.points: list[tuple[int, int]] = []

    def book(self, start: int, end: int) -> int:
        self.points.append((start, +1))
        self.points.append((end, -1))
        return self.max_booking()

    def max_booking(self) -> int:
        self.points.sort()

        max_found = 0
        current = 0

        for _, dx in self.points:
            current += dx
            max_found = max(max_found, current)

        return max_found
