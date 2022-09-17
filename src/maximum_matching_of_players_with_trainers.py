import copy
import heapq


class Solution:
    def matchPlayersAndTrainers(
        self, players: list[int], trainers: list[int]
    ) -> int:
        matches = 0

        players_heap: list[int] = copy.copy(players)
        trainers_heap: list[int] = copy.copy(trainers)

        heapq.heapify(players_heap)
        heapq.heapify(trainers_heap)

        while players_heap and trainers_heap:
            player = heapq.heappop(players_heap)
            trainer = heapq.heappop(trainers_heap)

            while player > trainer and trainers_heap:
                trainer = heapq.heappop(trainers_heap)

            if player <= trainer:
                matches += 1

        return matches
