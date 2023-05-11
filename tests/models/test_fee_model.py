from datetime import datetime, timedelta
from src.models.parking import Parking
from src.models.fee_model import AdditivePerHour, AdditiveIntervalThenHourly, IntervalsThenDaily
from src.models.vehicle_type import VehicleType


class TestAdditivePerHour:
    def __init__(self):
        pass

    def test_fee(self):
        two_wheeler_parking = Parking(VehicleType.TWO_WHEELER, 1, "001", hours_ago(4.1))
        four_wheeler_parking = Parking(VehicleType.FOUR_WHEELER, 1, "001", hours_ago(0.1))
        heavy_vehicle_parking = Parking(VehicleType.HEAVY_VEHICLE, 1, "001", hours_ago(1.99))
        model = AdditivePerHour({
            VehicleType.TWO_WHEELER: 100,
            VehicleType.FOUR_WHEELER: 200,
            VehicleType.HEAVY_VEHICLE: 300
        })

        assert model.fee(two_wheeler_parking) == 500
        assert model.fee(four_wheeler_parking) == 200
        assert model.fee(heavy_vehicle_parking) == 600

    def test_default_rates_fee(self):
        parking = Parking(VehicleType.TWO_WHEELER, 1, "001", hours_ago(4.1))
        assert AdditivePerHour().fee(parking) == 500

    def test_zero_hours_fee(self):
        parking = Parking(VehicleType.TWO_WHEELER, 1, "001", hours_ago(0))
        assert AdditivePerHour().fee(parking) == 0


class TestAdditiveIntervalThenHourly:
    def __init__(self):
        pass

    def test_fee(self):
        two_wheeler_parking1 = Parking(VehicleType.TWO_WHEELER, 1, "001", hours_ago(3.4))
        two_wheeler_parking2 = Parking(VehicleType.TWO_WHEELER, 1, "001", hours_ago(14.99))
        two_wheeler_parking3 = Parking(VehicleType.TWO_WHEELER, 1, "001", hours_ago(8))
        four_wheeler_parking = Parking(VehicleType.FOUR_WHEELER, 1, "001", hours_ago(11.5))
        heavy_vehicle_parking = Parking(VehicleType.HEAVY_VEHICLE, 1, "001", hours_ago(13.05))
        model = AdditiveIntervalThenHourly()

        assert model.fee(two_wheeler_parking1) == 30
        assert model.fee(two_wheeler_parking2) == 390
        assert model.fee(two_wheeler_parking3) == 90
        assert model.fee(four_wheeler_parking) == 180
        assert model.fee(heavy_vehicle_parking) is None

    def test_zero_hours_fee(self):
        parking = Parking(VehicleType.TWO_WHEELER, 1, "001", hours_ago(0))
        assert AdditivePerHour().fee(parking) == 0


class TestIntervalsThenDaily:
    def __init__(self):
        pass

    def test_fee(self):
        two_wheeler_parking1 = Parking(VehicleType.TWO_WHEELER, 1, "001", hours_ago(0.55))
        two_wheeler_parking2 = Parking(VehicleType.TWO_WHEELER, 1, "001", hours_ago(14.99))
        two_wheeler_parking3 = Parking(VehicleType.TWO_WHEELER, 1, "001", hours_ago(36))
        four_wheeler_parking1 = Parking(VehicleType.FOUR_WHEELER, 1, "001", hours_ago(0.5))
        four_wheeler_parking2 = Parking(VehicleType.FOUR_WHEELER, 1, "001", hours_ago(23.59))
        four_wheeler_parking3 = Parking(VehicleType.FOUR_WHEELER, 1, "001", hours_ago(73))
        heavy_vehicle_parking = Parking(VehicleType.HEAVY_VEHICLE, 1, "001", hours_ago(13.05))
        model = IntervalsThenDaily()

        assert model.fee(two_wheeler_parking1) == 0
        assert model.fee(two_wheeler_parking2) == 60
        assert model.fee(two_wheeler_parking3) == 140
        assert model.fee(four_wheeler_parking1) == 60
        assert model.fee(four_wheeler_parking2) == 80
        assert model.fee(four_wheeler_parking3) == 380
        assert model.fee(heavy_vehicle_parking) is None

    def test_zero_hours_fee(self):
        parking = Parking(VehicleType.TWO_WHEELER, 1, "001", hours_ago(0))
        assert IntervalsThenDaily().fee(parking) == 0


def hours_ago(hours):
    return datetime.now() - timedelta(hours=hours)
