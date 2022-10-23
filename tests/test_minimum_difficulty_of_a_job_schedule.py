import pytest

from src.minimum_difficulty_of_a_job_schedule import Solution


@pytest.mark.parametrize(
    "jobs,d,expected",
    [
        ([6, 5, 4, 3, 2, 1], 2, 7),
        ([6, 5, 4, 3, 2], 3, 11),
        ([9, 9, 9], 4, -1),
        ([1, 1, 1], 4, -1),
    ],
)
def test_solution(jobs, d, expected):
    assert Solution().minDifficulty(jobs, d) == expected
