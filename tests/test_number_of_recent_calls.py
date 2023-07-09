from src.number_of_recent_calls import RecentCounter


def test_solution():
    rc = RecentCounter()

    assert rc.ping(1) == 1
    assert rc.ping(100) == 2
    assert rc.ping(3001) == 3
    assert rc.ping(3002) == 3
