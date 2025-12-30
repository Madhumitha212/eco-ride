from abc import ABC, abstractmethod
import csv
import os
import json

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
    def __str__(self):
        return f"{self.vehicle_id} | {self.model} | {self.get_battery_percentage()}% | {self.status}"
    
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
    
    def categorize_by_type(self):
        categories = {"Car": [], "Scooter": []}
        for vehicles in self.fleet_hubs.values():
            for v in vehicles:
                if isinstance(v, ElectricCar):
                    categories["Car"].append(v)
                elif isinstance(v, ElectricScooter):
                    categories["Scooter"].append(v)
        return categories
    
    def fleet_analytics(self):
        summary = {"Available": 0, "On Trip": 0, "Under Maintenance": 0}
        for vehicles in self.fleet_hubs.values():
            for v in vehicles:
                summary[v.status] += 1
        return summary
    
    def sort_by_model(self, hub_name):
        self.fleet_hubs[hub_name].sort(key=lambda v: v.model)

    def sort_by_battery(self, hub_name):
        self.fleet_hubs[hub_name].sort(key=lambda v: v.get_battery_percentage(), reverse=True)

    def load_fleet_management_from_csv(self, filename="fleet_management.csv"):
        if not os.path.exists(filename):
            print("CSV not found. Starting with empty fleet.")
            return

        self.fleet_hubs = {}

        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                hub = row["Hub"]

                if hub not in self.fleet_hubs:
                    self.fleet_hubs[hub] = []

                if row["Type"] == "ElectricCar":
                    vehicle = ElectricCar(
                        row["Vehicle ID"],
                        row["Model"],
                        int(row["Battery"]),
                        seating_capacity=4
                    )
                else:
                    vehicle = ElectricScooter(
                        row["Vehicle ID"],
                        row["Model"],
                        int(row["Battery"]),
                        max_speed_limit=80
                    )

                self.fleet_hubs[hub].append(vehicle)

    def save_fleet_management_to_csv(self, filename="fleet_management.csv"):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Hub", "Vehicle ID", "Model", "Battery", "Type"])
            for hub, vehicles in self.fleet_hubs.items():
                for v in vehicles:
                    writer.writerow([
                        hub,
                        v.vehicle_id,
                        v.model,
                        v.get_battery_percentage(),
                        type(v).__name__
                    ])

    def load_fleet_management_from_json(self, filename="fleet_management.json"):
        if not os.path.exists(filename):
            print("JSON file not found. Starting with empty fleet.")
            return

        self.fleet_hubs = {}

        with open(filename, "r") as file:
            data = json.load(file)

            for hub, vehicles in data.items():
                self.fleet_hubs[hub] = []

                for v in vehicles:
                    if v["type"] == "ElectricCar":
                        vehicle = ElectricCar(
                            v["vehicle_id"],
                            v["model"],
                            v["battery_percentage"],
                            v["seating_capacity"]
                        )
                    elif v["type"] == "ElectricScooter":
                        vehicle = ElectricScooter(
                            v["vehicle_id"],
                            v["model"],
                            v["battery_percentage"],
                            v["max_speed_limit"]
                        )

                    self.fleet_hubs[hub].append(vehicle)
    
    def save_fleet_management_to_json(self, filename="fleet_management.json"):
        data = {}

        for hub, vehicles in self.fleet_hubs.items():
            data[hub] = []
            for v in vehicles:
                vehicle_data = {
                    "type": type(v).__name__,
                    "vehicle_id": v.vehicle_id,
                    "model": v.model,
                    "battery_percentage": v.get_battery_percentage()
                }

                # Serialize subclass-specific fields
                if isinstance(v, ElectricCar):
                    vehicle_data["seating_capacity"] = v.seating_capacity
                elif isinstance(v, ElectricScooter):
                    vehicle_data["max_speed_limit"] = v.max_speed_limit

                data[hub].append(vehicle_data)

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
            
