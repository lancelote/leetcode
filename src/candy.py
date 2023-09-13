class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        result = [1] * n

        for i in range(n - 1):
            if ratings[i] < ratings[i + 1]:
                result[i + 1] = max(1 + result[i], result[i + 1])

        for i in range(n - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                result[i] = max(1 + result[i + 1], result[i])

        return sum(result)
