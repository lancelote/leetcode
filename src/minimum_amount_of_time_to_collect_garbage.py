class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        n = len(garbage)
        travel.append(0)

        def count_path(trash: str) -> int:
            i = 0
            path = 0
            total = 0

            while i < n:
                count = garbage[i].count(trash)

                if count:
                    total += count + path
                    path = 0
                path += travel[i]

                i += 1

            return total

        return sum(count_path(x) for x in "MPG")
