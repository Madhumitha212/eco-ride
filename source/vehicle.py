from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,vehicle_id, model,battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = battery_percentage
        self.set_battery_percentage(battery_percentage)

    def get_battery_percentage(self):
        return self.__battery_percentage
    def set_battery_percentage(self,battery_percentage):
        if 0<=battery_percentage <= 100:
            self.__battery_percentage = battery_percentage
        else:
            print("Invalid battery percentage! Must be between 0 and 100:")

    @abstractmethod
    def calculate_trip_cost(self,distance):
        pass

class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage,seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = seating_capacity

    def calculate_trip_cost(self, distance):
        return 5.0 + (0.5 * distance)
    
class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage,max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit = max_speed_limit

    def calculate_trip_cost(self, distance):
        return 1.0 + (0.15 * distance)
    
def create_fleet_hubs(self):
        fleet_hubs = {}

        fleet_hubs["Downtown"] = []
        fleet_hubs["Airport"] = []

        car1 = ElectricCar("EC601", "Tesla Model 3", 90, 5)
        car2 = ElectricCar("EC602", "Tesla Model Y", 85, 7)
        scooter1 = ElectricScooter("ES603", "Ather 450X", 80, 85)

        fleet_hubs["Downtown"].append(car1)
        fleet_hubs["Downtown"].append(scooter1)
        fleet_hubs["Airport"].append(car2)

        for hub_name, vehicles in fleet_hubs.items():
            print(f"\nHub: {hub_name}")
            for vehicle in vehicles:
                print(vehicle)

        return fleet_hubs