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