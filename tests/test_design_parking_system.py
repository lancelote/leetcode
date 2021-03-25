from src.design_parking_system import ParkingSystem


def test_solution():
    parking = ParkingSystem(1, 1, 0)

    assert parking.addCar(1) is True
    assert parking.addCar(2) is True
    assert parking.addCar(3) is False
    assert parking.addCar(1) is False
