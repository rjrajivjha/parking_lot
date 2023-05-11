from models.parking_lot import ParkingLot
from models.fee_model import AdditivePerHour
from models.vehicle_type import VehicleType

# Mocks example 1 from the problem statement.
class Example1():
    INSTRUCTIONS = [
        "park,Motorcycle",
        "park,Scooter",
        "park,Scooter",
        "park,Bus",
        "unpark,003",
        "unpark,002",
        "unpark,001"
    ]
    
    VEHICLE_TYPE_BY_COMMON_NAME = {
        "motorcycle": VehicleType.TWO_WHEELER,
        "scooter": VehicleType.TWO_WHEELER,
        "car": VehicleType.FOUR_WHEELER,
        "suv": VehicleType.FOUR_WHEELER,
        "bus": VehicleType.HEAVY_VEHICLE,
        "truck": VehicleType.HEAVY_VEHICLE
    }
    
    def run(self):
        lot = ParkingLot(
            "Small motorcycle/scooter parking lot",
            AdditivePerHour(),
            {
                VehicleType.TWO_WHEELER: 2,
                VehicleType.FOUR_WHEELER: 0
            }
        )
        self.execute_instructions(lot)
    
    def execute_instructions(self, lot):
        for instruction_string in self.INSTRUCTIONS:
            print(instruction_string)
            tokens = instruction_string.split(",")
            instruction = tokens[0]
            
            if instruction == "park":
                vehicle_name = tokens[1].lower()
                vehicle_type = self.VEHICLE_TYPE_BY_COMMON_NAME[vehicle_name]
                parking = lot.park_vehicle(vehicle_type)
                if not parking:
                    print("No space available to park {}\n".format(tokens[1]))
                else:
                    self.display_ticket(parking)
                    
            elif instruction == "unpark":
                ticket_number = tokens[1]
                parking = lot.unpark_vehicle(ticket_number)
                if not parking:
                    print("Could not find vehicle for {}\n".format(ticket_number))
                else:
                    self.display_receipt(parking)

            else:
                raise "Invalid instruction"
            
    def display_ticket(self, parking):
        print(
            "\n".join([
            "Parking Ticket: {}".format(parking.ticket_number),
            "Parking Slot: {}".format(parking.slot),
            "Vehicle Type: {}".format(parking.vehicle_type.value),
            "Entry time: {}\n".format(parking.entry_time.strftime("%m/%d/%Y, %H:%M"))
            ])
        )
        
    def display_receipt(self, parking):
        print(
            "\n".join([
            "Parking Ticket: {}".format(parking.ticket_number),
            "Receipt Number: {}".format(parking.receipt.number),
            "Entry time: {}".format(parking.entry_time.strftime("%m/%d/%Y, %H:%M")),
            "Exit time: {}".format(parking.exit_time.strftime("%m/%d/%Y, %H:%M")),
            "Fee: {}\n".format(parking.receipt.fee)
            ])
        )

if __name__ == '__main__':
    Example1().run()