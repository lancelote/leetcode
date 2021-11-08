class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        sorted_seats = sorted(seats)
        sorted_students = sorted(students)

        return sum(
            abs(seat - student)
            for (seat, student) in zip(sorted_seats, sorted_students)
        )
