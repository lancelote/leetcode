import pytest

from src.defanging_an_ip_address import Solution


@pytest.mark.parametrize(
    "address,expected",
    [
        ("1.1.1.1", "1[.]1[.]1[.]1"),
        ("255.100.50.0", "255[.]100[.]50[.]0"),
    ],
)
def test_solution(address, expected):
    assert Solution().defangIPaddr(address) == expected
