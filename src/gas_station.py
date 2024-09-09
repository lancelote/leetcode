class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        answer = 0
        total = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff

            if total < 0:
                total = 0
                answer = i + 1

        return answer
