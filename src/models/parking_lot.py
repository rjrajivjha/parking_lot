from .slot_set import SlotSet
from .parking import Parking


class ParkingLot:
    def __init__(self, name, fee_model, capacity_by_type):
        self.name = name
        self.fee_model = fee_model
        self.slot_set = SlotSet(capacity_by_type)
        self.parkingsByTicketNumber = {}
        self.current_ticket_number = 0

    def park_vehicle(self, vehicle_type):
        slot = self.slot_set.assign_slot(vehicle_type)
        if slot:
            parking = Parking(
                vehicle_type,
                slot,
                self.__next_ticket_number()
            )
            self.__index_by_ticket_number(parking)
            return parking

    def unpark_vehicle(self, ticket_number):
        parking = self.__get_parking(ticket_number)
        if parking:
            self.slot_set.vacate_slot(parking.slot)
            parking.unpark(self.fee_model.fee(parking))
            return parking

    def __get_parking(self, ticket_number):
        return self.parkingsByTicketNumber.get(ticket_number, None)

    def __index_by_ticket_number(self, parking):
        self.parkingsByTicketNumber[parking.ticket_number] = parking

    def __next_ticket_number(self):
        self.current_ticket_number += 1
        return "00{}".format(self.current_ticket_number)
