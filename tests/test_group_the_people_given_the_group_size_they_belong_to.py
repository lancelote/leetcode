import pytest

from src.group_the_people_given_the_group_size_they_belong_to import Solution


@pytest.mark.parametrize(
    "groupSizes,expected",
    (
        ([3, 3, 3, 3, 3, 1, 3], [[3, 4, 6], [3, 4, 6], [5]]),
        ([2, 1, 3, 3, 3, 2], [[0, 5], [1], [2, 3, 4]]),
    ),
)
def test_solution(groupSizes, expected):
    assert Solution().groupThePeople(groupSizes) == expected
