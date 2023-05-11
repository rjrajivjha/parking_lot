from src.models.parking_lot import ParkingLot
from src.models.vehicle_type import VehicleType
from src.models.fee_model import AdditivePerHour
import pytest


@pytest.fixture
def mall_parking_lot():
    return ParkingLot(
        "Mall",
        AdditivePerHour({
            VehicleType.TWO_WHEELER: 10,
            VehicleType.FOUR_WHEELER: 20
        }),
        {
            VehicleType.TWO_WHEELER: 2,
            VehicleType.FOUR_WHEELER: 3
        }
    )


@pytest.mark.usefixtures("mall_parking_lot")
class TestParkingLot:
    def __init__(self):
        pass

    def test_init(self, mall_parking_lot):
        lot = mall_parking_lot
        assert lot.name == "Mall"
        assert lot.fee_model.rate_chart == {
            VehicleType.TWO_WHEELER: 10,
            VehicleType.FOUR_WHEELER: 20,
            # VehicleType.HEAVY_VEHICLE: None
        }
        assert lot.slot_set.slots_by_type == {
            VehicleType.TWO_WHEELER: {1, 2},
            VehicleType.FOUR_WHEELER: {3, 4, 5},
            # VehicleType.HEAVY_VEHICLE: 0
        }

    def test_parking_when_empty(self, mall_parking_lot):
        lot = mall_parking_lot
        vehicle_type = VehicleType.TWO_WHEELER
        parking = lot.park_vehicle(vehicle_type)
        assert parking
        assert parking.vehicle_type == VehicleType.TWO_WHEELER
        assert parking.ticket_number == "001"
        assert list(lot.parkingsByTicketNumber.values())[0].ticket_number == parking.ticket_number

    def test_parking_when_full(self, mall_parking_lot):
        lot = mall_parking_lot
        vehicle_type = VehicleType.TWO_WHEELER
        lot.slot_set.available_slots = {
            VehicleType.TWO_WHEELER: set(),
        }
        parking = lot.park_vehicle(vehicle_type)
        assert parking == None
        assert lot.parkingsByTicketNumber == {}

    def test_parking_when_other_type_full(self, mall_parking_lot):
        lot = mall_parking_lot
        vehicle_type = VehicleType.TWO_WHEELER
        lot.slot_set.available_slots[VehicleType.FOUR_WHEELER] = set()
        parking = lot.park_vehicle(vehicle_type)
        assert parking

    def test_unparking(self, mall_parking_lot):
        lot = mall_parking_lot
        parking = lot.park_vehicle(VehicleType.TWO_WHEELER)
        lot.unpark_vehicle(parking.ticket_number)
        assert parking.receipt.fee == 10
