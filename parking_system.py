class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.capacity = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.capacity[carType - 1] > 0:
            self.capacity[carType - 1] -= 1
            return True
        else:
            return False


parking_system = ParkingSystem(1, 1, 0)
assert parking_system.addCar(1)
assert parking_system.addCar(2)
assert not parking_system.addCar(3)
assert not parking_system.addCar(1)
