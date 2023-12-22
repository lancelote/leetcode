import pytest

from src.course_schedule import Solution


@pytest.mark.parametrize(
    "num_courses,prereqs,expected",
    [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (3, [[2, 1], [1, 0]], True),
    ],
)
def test_solution(num_courses, prereqs, expected):
    assert Solution().canFinish(num_courses, prereqs) is expected
