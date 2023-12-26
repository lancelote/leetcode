class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = len(rooms)
        visited = {0}
        to_visit = rooms[0]

        while to_visit:
            room = to_visit.pop()
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    to_visit.append(key)

        return len(visited) == n
