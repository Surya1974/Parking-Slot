class ParkingSlot:

    def __init__(self, level: str, spot: int) -> None:
        self.level = level
        self.spot = spot
        self.vehicle = ''

    def setVehicle(self, vehicle: str) -> None:
        self.vehicle = vehicle