class Solution:
    def aggregateTimeSeries(
        self, series1: list[list[int]], series2: list[list[int]]
    ) -> list[list[int]]:
        n1 = len(series1)
        n2 = len(series2)

        idx1 = idx2 = 0

        result: list[list[int]] = []

        while idx1 < n1 and idx2 < n2:
            timestamp1, value1 = series1[idx1]
            timestamp2, value2 = series2[idx2]

            if timestamp1 < timestamp2:
                idx1 += 1
            elif timestamp1 > timestamp2:
                idx2 += 1
            else:
                idx1 += 1
                idx2 += 1

            result.append([min(timestamp1, timestamp2), value1 + value2])

        while idx1 < n1:
            result.append(series1[idx1])
            idx1 += 1

        while idx2 < n2:
            result.append(series2[idx2])
            idx2 += 1

        return result
