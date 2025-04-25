print("Open-Ended Lab-Ten")
print("Welcome to Smart City Parking System\n")

# Vehicle class
class Vehicle:
    def __init__(self, v_type, plate, priority=False):
        self.type = v_type
        self.plate = plate
        self.priority = priority

# Slot class
class Slot:
    def __init__(self, zone, level, number, vtype, is_priority=False):
        self.zone = zone
        self.level = level
        self.number = number
        self.vtype = vtype
        self.priority = is_priority
        self.occupied = False
        self.vehicle = None

# Main Parking System
class ParkingSystem:
    def __init__(self):
        self.slots = []  # all slots
        self.parked = {}  # plate number -> slot

    def add_slots(self):
        zones = ['A', 'B']
        for z in zones:
            for l in range(1, 3):  # Levels 1 & 2
                for s in range(1, 4):  # 3 slots per type
                    for typ in ['Bike', 'Car', 'Truck']:
                        is_p = (s == 1)  # slot 1 is priority
                        new_slot = Slot(z, l, s, typ, is_p)
                        self.slots.append(new_slot)

    def park_vehicle(self, vehicle):
        for slot in self.slots:
            if not slot.occupied and slot.vtype == vehicle.type:
                if vehicle.priority and not slot.priority:
                    continue
                slot.occupied = True
                slot.vehicle = vehicle
                self.parked[vehicle.plate] = slot
                print(f"Allocated Slot: Zone {slot.zone} - Level {slot.level} - Slot {slot.number}")
                return
        print("No slot available for this vehicle.")

    def remove_vehicle(self, plate):
        if plate in self.parked:
            slot = self.parked[plate]
            slot.occupied = False
            slot.vehicle = None
            del self.parked[plate]
            print("Vehicle removed.")
        else:
            print("Vehicle not found.")

    def show_all(self):
        for slot in self.slots:
            stat = "Occupied" if slot.occupied else "Available"
            print(f"Zone {slot.zone} | Level {slot.level} | Slot {slot.number} | {slot.vtype} | {stat}")

    def show_ev_slots(self):
        for slot in self.slots:
            if slot.priority and not slot.occupied:
                print(f"Available EV/Priority Slot: Zone {slot.zone} Level {slot.level} Slot {slot.number}")

    def show_priority_vehicles(self):
        for slot in self.slots:
            if slot.occupied and slot.vehicle.priority:
                print(f"Priority Vehicle: {slot.vehicle.plate} in Zone {slot.zone} Level {slot.level} Slot {slot.number}")

# Initialize parking system
psys = ParkingSystem()
psys.add_slots()

# Menu
while True:
    print("\n1. Park a Vehicle")
    print("2. Remove a Vehicle")
    print("3. Show All Parking Slots")
    print("4. Show Available Slots for EVs")
    print("5. Show Priority Vehicles")
    print("6. Exit")
    
    ch = input("Choose Option: ")

    if ch == '1':
        typ = input("Enter Vehicle Type (Bike/Car/Truck): ")
        plate = input("Enter Plate Number: ")
        pr = input("Priority? (Y/N): ")
        vehicle = Vehicle(typ, plate, pr.upper() == 'Y')
        psys.park_vehicle(vehicle)

    elif ch == '2':
        p = input("Enter Plate Number: ")
        psys.remove_vehicle(p)

    elif ch == '3':
        psys.show_all()

    elif ch == '4':
        psys.show_ev_slots()

    elif ch == '5':
        psys.show_priority_vehicles()

    elif ch == '6':
        print("Lab completed successfully.")
        break

    else:
        print("Invalid option.")
