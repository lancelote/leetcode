import pytest

from src.poor_pigs import Solution


@pytest.mark.parametrize(
    "buckets,min_to_die,min_to_test,expected",
    ((4, 15, 15, 2), (4, 15, 30, 2), (125, 1, 4, 3)),
)
def test_solution(buckets, min_to_die, min_to_test, expected):
    assert Solution().poorPigs(buckets, min_to_die, min_to_test) == expected
