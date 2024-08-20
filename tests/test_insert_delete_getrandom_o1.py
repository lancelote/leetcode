import pytest

from src.insert_delete_getrandom_o1 import RandomizedSet


@pytest.fixture
def rs() -> RandomizedSet:
    return RandomizedSet()


def test_basic_example(rs):
    assert rs.insert(1)
    assert rs.remove(2) is False
    assert rs.insert(2)
    assert rs.getRandom() in {1, 2}
    assert rs.remove(1)
    assert rs.insert(2) is False
    assert rs.getRandom() == 2


def test_remove_only_item(rs):
    assert rs.remove(0) is False
    assert rs.remove(0) is False
    assert rs.insert(0)
    assert rs.getRandom() == 0
    assert rs.remove(0)
    assert rs.insert(0)


def test_delete_last_inserted(rs):
    assert rs.insert(1)
    assert rs.insert(2)
    assert rs.remove(2)
