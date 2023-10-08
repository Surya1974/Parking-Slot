from ParkingSlot import ParkingSlot

class ParkingSpace:

    MAX_SLOTS = 40

    def __init__(self):
        self.levels = {}
        self.levels["A"] = [ParkingSlot("A", i) for i in range(1, 21)]
        self.levels["B"] = [ParkingSlot("B", i) for i in range(21, 41)]
        self.dict = {}

    def assignParkingSlot(self, vehicleNumber: str) -> None:
        if len(self.dict.keys()) == ParkingSpace.MAX_SLOTS:
            raise Exception("Parking slots are not available.")

        if vehicleNumber in self.dict:
            raise Exception("Vehicle is already parked.")

        for level in ["A", "B"]:
            for slot in self.levels[level]:
                if not slot.vehicle:
                    slot.setVehicle(vehicleNumber)
                    self.dict[vehicleNumber] = slot
                    return

    def retrieveParkingSlot(self, vehicleNumber: str):
        if vehicleNumber in self.dict:
            return self.dict[vehicleNumber]
        raise Exception("Vehicle isn't parked in the parking space.")