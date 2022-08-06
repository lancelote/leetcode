import pytest

from src.task_scheduler_ii import Solution


@pytest.mark.parametrize(
    "tasks,space,days_expected",
    [
        ([1, 2, 1, 2, 3, 1], 3, 9),
        ([5, 8, 8, 5], 2, 6),
        ([4, 10, 10, 9, 10, 4, 10, 4], 8, 30),
    ],
)
def test_solution(tasks, space, days_expected):
    assert Solution().taskSchedulerII(tasks, space) == days_expected
