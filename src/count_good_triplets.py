class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        good = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if all(
                        (
                            abs(arr[i] - arr[j]) <= a,
                            abs(arr[j] - arr[k]) <= b,
                            abs(arr[i] - arr[k]) <= c,
                        )
                    ):
                        good += 1
        return good
