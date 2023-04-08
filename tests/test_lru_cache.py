from src.lru_cache import LRUCache


def test_solution_1():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)

    assert cache.get(1) == 1

    cache.put(3, 3)

    assert cache.get(2) == -1

    cache.put(4, 4)

    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test_solution_2():
    cache = LRUCache(2)
    cache.put(1, 0)
    cache.put(2, 2)

    assert cache.get(1) == 0

    cache.put(3, 3)

    assert cache.get(2) == -1

    cache.put(4, 4)

    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test_solution_3():
    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(2, 2)

    assert cache.get(2) == 2

    cache.put(1, 1)
    cache.put(4, 1)

    assert cache.get(2) == -1
