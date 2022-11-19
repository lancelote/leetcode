class Solution:
    def is_clockwise(self, a: list[int], b: list[int], c: list[int]) -> bool:
        ax, ay = a
        bx, by = b
        cx, cy = c

        return (by - ay) * (cx - bx) - (bx - ax) * (cy - by) > 0

    def outerTrees(self, trees: list[list[int]]) -> list[list[int]]:
        stack: list[list[int]] = []
        points = sorted(trees)

        for i in range(len(points)):
            while len(stack) >= 2 and self.is_clockwise(
                stack[-2], stack[-1], points[i]
            ):
                stack.pop()
            stack.append(points[i])

        stack.pop()

        for i in range(len(points) - 1, -1, -1):
            while len(stack) >= 2 and self.is_clockwise(
                stack[-2], stack[-1], points[i]
            ):
                stack.pop()
            stack.append(points[i])

        seen: set[tuple[int, int]] = set()
        result: list[list[int]] = []

        for x, y in stack:
            if (x, y) not in seen:
                seen.add((x, y))
                result.append([x, y])

        return result
