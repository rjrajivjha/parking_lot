from src.models.parking import Parking, ParkingStatus
from src.models.vehicle_type import VehicleType
import pytest

class TestParking:
    def test_init(self):
        parking = Parking(VehicleType.TWO_WHEELER, 1, "001")
        assert parking.status == ParkingStatus.PARKED
        assert parking.slot == 1
        assert parking.vehicle_type == VehicleType.TWO_WHEELER
        assert parking.ticket_number == "001"
        assert parking.receipt == None
    
    def test_unpark(self):
        parking = Parking(VehicleType.TWO_WHEELER, 1, "001")
        parking.unpark(1000)
        assert parking.status == ParkingStatus.UNPARKED
        assert parking.receipt.fee == 1000