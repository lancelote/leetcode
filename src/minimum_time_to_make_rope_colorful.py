class Solution:
    def minCost(self, colors: str, needed_time: list[int]) -> int:
        assert needed_time

        result = 0
        current_max = needed_time[0]
        current_total = needed_time[0]
        current_count = 1

        for i in range(1, len(colors)):
            if colors[i] != colors[i - 1]:
                if current_count != 1:
                    result += current_total - current_max

                current_total = needed_time[i]
                current_max = needed_time[i]
                current_count = 1
            else:
                current_max = max(current_max, needed_time[i])
                current_total += needed_time[i]
                current_count += 1

        if current_count != 1:
            result += current_total - current_max
        return result
