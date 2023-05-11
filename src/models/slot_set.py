class SlotSet:
    def __init__(self, size_by_type):
        self.slots_by_type = self.slots_by_type(size_by_type)
        self.available_slots = self.slots_by_type
        self.taken_slots = {type: set() for type in self.slots_by_type.keys()}
        self.type_by_slot = self.type_by_slot(self.slots_by_type)

    def assign_slot(self, vehicle_type):
        if self.available_slots.get(vehicle_type):
            slot = self.available_slots[vehicle_type].pop()
            self.taken_slots[vehicle_type].add(slot)
            return slot

    def vacate_slot(self, slot):
        vehicle_type = self.type_by_slot[slot]
        if slot in self.taken_slots.get(vehicle_type):
            self.taken_slots[vehicle_type].remove(slot)
            self.available_slots[vehicle_type].add(slot)
            return slot
  
    def slots_by_type(self, size_by_type):
        slot_numbers = {}
        slot_count = 1

        for vehicle_type, capacity in size_by_type.items():
            slots = set(range(slot_count, slot_count + capacity))
            slot_numbers[vehicle_type] = slots
            slot_count += capacity

        return slot_numbers

    def type_by_slot(self, slots_by_type):
        result = {}
        for vehicle_type, slots in slots_by_type.items():
            for slot in slots:
                result[slot] = vehicle_type
        return result