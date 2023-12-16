from src.design_hashset import MyHashSet


def test_my_hash_set_0():
    hs = MyHashSet()
    hs.add(1)
    hs.add(2)

    assert hs.contains(1)
    assert hs.contains(3) is False

    hs.add(2)

    assert hs.contains(2)

    hs.remove(2)

    assert hs.contains(2) is False


def test_my_hash_set_1():
    hs = MyHashSet()
    hs.remove(1)
    hs.add(9)
    hs.remove(24)
    hs.add(53)
    hs.add(84)
    hs.remove(90)
    hs.add(34)

    assert hs.contains(9)

    hs.add(39)

    assert hs.contains(84)

    hs.add(18)

    assert hs.contains(9)

    hs.remove(2)
    hs.remove(34)

    assert hs.contains(18)


def test_resize():
    hs = MyHashSet()
    hs.add(1)
    hs.remove(1)
    hs.resize()
