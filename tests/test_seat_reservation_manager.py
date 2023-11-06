from src.seat_reservation_manager import SeatManager


def test_seat_manager():
    sm = SeatManager(5)

    assert sm.reserve() == 1
    assert sm.reserve() == 2

    sm.unreserve(2)

    assert sm.reserve() == 2
    assert sm.reserve() == 3
    assert sm.reserve() == 4
    assert sm.reserve() == 5

    sm.unreserve(5)
