class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack: list[tuple[int, int]] = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                old_i, old_temp = stack.pop()
                result[old_i] = i - old_i
            stack.append((i, temp))

        return result
