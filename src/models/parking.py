import uuid
from datetime import datetime
from enum import Enum
from .slot_set import SlotSet
from .vehicle_type import VehicleType
from .duration import Duration


class ParkingReceipt:
    def __init__(self, fee: float):
        self.number = self.generate_receipt_number()
        self.fee = fee

    def generate_receipt_number(self):
        return uuid.uuid4()


class ParkingStatus(Enum):
    PARKED = "PARKED"
    UNPARKED = "UNPARKED"


class Parking():
    def __init__(self, vehicle_type: VehicleType, slot, ticket_number, entry_time=datetime.now()):
        self.status = ParkingStatus.PARKED
        self.slot = slot
        self.vehicle_type = vehicle_type
        self.receipt = None
        self.ticket_number = ticket_number
        self.entry_time = entry_time
        self.exit_time = None

    def duration(self):
        return Duration(self.entry_time, self.exit_time or datetime.now())

    def generate_receipt(self, fee: float):
        self.receipt = ParkingReceipt(fee)

    def unpark(self, fee, exit_time=datetime.now()):
        self.status = ParkingStatus.UNPARKED
        self.exit_time = exit_time
        self.generate_receipt(fee)
