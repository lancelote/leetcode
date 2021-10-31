class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        return abs(sum(seats) - sum(students))
