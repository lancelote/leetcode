from collections import deque


class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        bank_set = set(bank)
        queue = deque([(start, 0)])
        seen = {start}

        while queue:
            state, steps = queue.popleft()

            if state == end:
                return steps

            for char in "ACGT":
                for i in range(len(state)):
                    new_state = state[:i] + char + state[i + 1 :]
                    if new_state not in seen and new_state in bank_set:
                        queue.append((new_state, steps + 1))
                        seen.add(new_state)

        return -1
