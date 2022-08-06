class Solution:
    def taskSchedulerII(self, tasks: list[int], space: int) -> int:
        day = 0
        history: dict[int, int] = {}

        for task_i, task in enumerate(tasks):
            if task in history and day - history[task] <= space:
                day += space - (day - history[task]) + 1
            history[task] = day
            day += 1

        return day
