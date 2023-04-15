import pytest

from src.convert_the_temperature import Solution


@pytest.mark.parametrize(
    "celsius,expected",
    [
        (36.50, [309.65000, 97.70000]),
        (122.11, [395.26000, 251.79800]),
    ],
)
def test_solution(celsius, expected):
    assert Solution().convertTemperature(celsius) == expected
