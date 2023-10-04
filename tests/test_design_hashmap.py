from src.design_hashmap import MyHashMap


def test_my_hash_map():
    h = MyHashMap()
    h.put(1, 1)
    h.put(2, 2)

    assert h.get(1) == 1
    assert h.get(3) == -1

    h.put(2, 1)

    assert h.get(2) == 1

    h.remove(2)

    assert h.get(2) == -1

    h.remove(3)
