class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int) -> None:
        self.parking = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.parking[carType] == 0:
            return False
        self.parking[carType] -= 1
        return True
