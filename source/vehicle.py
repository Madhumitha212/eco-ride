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
    def __eq__(self, other):
        return isinstance(other, Vehicle) and self.vehicle_id == other.vehicle_id
    
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
    
class FleetManager:
    def __init__(self):
        self.fleet_hubs = {}

    def add_hub(self, hub_name):
        if hub_name not in self.fleet_hubs:
            self.fleet_hubs[hub_name] = []

    def add_vehicle_to_hub(self, hub_name, vehicle):
        if any(v == vehicle for v in self.fleet_hubs.get(hub_name, [])):
            return False
        self.fleet_hubs[hub_name].append(vehicle)
        return True
    
    def search_by_hub(self, hub_name):
        return self.fleet_hubs.get(hub_name, [])

    def search_high_battery(self, threshold=80):
        return [v for vehicles in self.fleet_hubs.values() for v in vehicles if v.get_battery_percentage() > threshold]