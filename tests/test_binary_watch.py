import pytest

from src.binary_watch import Solution


@pytest.mark.parametrize(
    "turned_on,expected",
    (
        (
            1,
            [
                "0:01",
                "0:02",
                "0:04",
                "0:08",
                "0:16",
                "0:32",
                "1:00",
                "2:00",
                "4:00",
                "8:00",
            ],
        ),
        (9, []),
    ),
)
def test_solution(turned_on, expected):
    actual = Solution().readBinaryWatch(turned_on)

    assert len(actual) == len(expected)
    assert set(actual) == set(expected)
