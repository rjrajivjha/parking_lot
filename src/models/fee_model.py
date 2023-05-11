from abc import ABC, abstractmethod
import math
from .parking import Parking
from .vehicle_type import VehicleType


class FeeModel(ABC):
    def __init__(self, rate_chart=None):
        self.rate_chart = rate_chart or self.default_rate_chart()

    @abstractmethod
    def default_rate_chart(self):
        pass

    @abstractmethod
    def fee(self, parking: Parking):
        pass


class AdditivePerHour(FeeModel):
    def default_rate_chart(self):
        return {
            VehicleType.TWO_WHEELER: 10,
            VehicleType.FOUR_WHEELER: 20,
            VehicleType.HEAVY_VEHICLE: 50
        }

    def fee(self, parking: Parking):
        hourly_rate = self.rate_chart[parking.vehicle_type]
        return parking.duration().hours() * hourly_rate


class AdditiveIntervalThenHourly(FeeModel):
    def default_rate_chart(self):
        return {
            VehicleType.TWO_WHEELER: {
                "flat_fee_interval_hours": {
                    (0, 4): 30,
                    (4, 12): 60
                },
                "hourly_rates_after_hours": 12,
                "hourly_rate": 100
            },
            VehicleType.FOUR_WHEELER: {
                "flat_fee_interval_hours": {
                    (0, 4): 60,
                    (4, 12): 120
                },
                "hourly_rates_after_hours": 12,
                "hourly_rate": 200
            },
            VehicleType.HEAVY_VEHICLE: None
        }

    def fee(self, parking: Parking):
        chart = self.rate_chart[parking.vehicle_type]
        if not chart: return None
        duration = parking.duration().hours()
        flat_fee_chart = chart["flat_fee_interval_hours"].items()
        hourly_rate_start = chart["hourly_rates_after_hours"]
        hourly_rate = chart["hourly_rate"]

        fee = 0
        for (start, _), rate in flat_fee_chart:
            if start < duration:
                fee += rate

        if duration > hourly_rate_start:
            hourly_rateHours = duration - hourly_rate_start
            fee += hourly_rateHours * hourly_rate

        return fee


class IntervalsThenDaily(FeeModel):
    def default_rate_chart(self):
        return {
            VehicleType.TWO_WHEELER: {
                "flat_fee_upto_hours": {
                    1: 0,
                    8: 40,
                    24: 60
                },
                "daily_rates_after_days": 1,
                "daily_rate": 80
            },
            VehicleType.FOUR_WHEELER: {
                "flat_fee_upto_hours": {
                    12: 60,
                    24: 80
                },
                "daily_rates_after_days": 1,
                "daily_rate": 100
            },
            VehicleType.HEAVY_VEHICLE: None
        }

    def fee(self, parking: Parking):
        chart = self.rate_chart[parking.vehicle_type]
        if not chart: return None
        duration = parking.duration().hours()
        flat_fee_chart = chart["flat_fee_upto_hours"]
        daily_rate_start = chart["daily_rates_after_days"]
        daily_rate = chart["daily_rate"]

        endHour = self.__bucket_by_upper_limit(duration, flat_fee_chart.keys())
        fee = flat_fee_chart[endHour]

        days = math.ceil(float(duration) / 24)
        if days > daily_rate_start:
            daily_rate_days = days - daily_rate_start
            fee += daily_rate_days * daily_rate

        return fee

    def __bucket_by_upper_limit(self, element, bucket_limits):
        alist = list(bucket_limits)
        alist.sort()
        for limit in bucket_limits:
            if element <= limit:
                return limit
        return alist[-1]
