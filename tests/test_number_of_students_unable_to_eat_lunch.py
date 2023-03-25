import pytest

from src.number_of_students_unable_to_eat_lunch import Solution


@pytest.mark.parametrize(
    "students,sandwiches,expected",
    [
        ([1, 1, 0, 0], [0, 1, 0, 1], 0),
        ([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1], 3),
    ],
)
def test_solution(students, sandwiches, expected):
    assert Solution().countStudents(students, sandwiches) == expected
