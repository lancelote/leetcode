class Solution:
    def findCircleNum(self, is_connected: list[list[int]]) -> int:
        n = len(is_connected)
        count = 0
        seen: set[int] = set()

        def visit(city: int) -> None:
            if city in seen:
                return

            seen.add(city)

            for neighbor, val in enumerate(is_connected[city]):
                if val and neighbor not in seen:
                    visit(neighbor)

        for i in range(n):
            if i not in seen:
                count += 1
                visit(i)

        return count
