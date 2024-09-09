class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        result = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1] and result[i] <= result[i - 1]:
                result[i] = result[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and result[i] <= result[i + 1]:
                result[i] = result[i + 1] + 1

        return sum(result)
