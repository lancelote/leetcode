class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        result = [0] * n
        stack: list[tuple[int, int]] = []

        for i, x in enumerate(temperatures):
            while stack and x > stack[-1][1]:
                prev_i, _ = stack.pop()
                result[prev_i] = i - prev_i
            stack.append((i, x))

        return result
