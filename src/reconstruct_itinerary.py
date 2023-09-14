from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        dep_to_arr: dict[str, list[str]] = defaultdict(list)

        for dep, arr in sorted(tickets, reverse=True):
            dep_to_arr[dep].append(arr)

        result = []
        stack = ["JFK"]

        while stack:
            while dep_to_arr[stack[-1]]:
                stack.append(dep_to_arr[stack[-1]].pop())
            result.append(stack.pop())

        return result[::-1]
