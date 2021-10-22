class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:
        max_length = 0
        count = 0

        for rectangle in rectangles:
            shortest_side = min(rectangle)
            if shortest_side > max_length:
                max_length = shortest_side
                count = 1
            elif shortest_side == max_length:
                count += 1

        return count
