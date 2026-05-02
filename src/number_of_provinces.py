class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        result = 0
        seen: set[int] = set()

        def dfs(city: int) -> None:
            if city in seen:
                return

            seen.add(city)

            for other in range(len(isConnected)):
                if isConnected[city][other]:
                    dfs(other)

        for i in range(len(isConnected)):
            if i not in seen:
                dfs(i)
                result += 1

        return result
