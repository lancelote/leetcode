import pytest

from src.destination_city import Solution


@pytest.mark.parametrize(
    "paths,expected",
    [
        (
            [
                ["London", "New York"],
                ["New York", "Lima"],
                ["Lima", "Sao Paulo"],
            ],
            "Sao Paulo",
        ),
        ([["B", "C"], ["D", "B"], ["C", "A"]], "A"),
        ([["A", "Z"]], "Z"),
    ],
)
def test_solution(paths, expected):
    assert Solution().destCity(paths) == expected
