import unittest
from vehicle import*

class TestFleetManager(unittest.TestCase):

    def setUp(self):
        self.manager = FleetManager()
        self.car = ElectricCar("EC101", "Tesla Model 3", 90, 5)
        self.scooter = ElectricScooter("ES201", "Ather", 70, 85)
        self.car1 = ElectricCar("EC102", "Nissan Leaf", 60, 4)
        self.scooter1 = ElectricScooter("ES201", "Ather", 85, 85)

        self.manager.add_hub("Hub1")
        self.manager.add_vehicle_to_hub("Hub1", self.car)
        self.manager.add_vehicle_to_hub("Hub1", self.car1)
        self.manager.add_vehicle_to_hub("Hub1", self.scooter)
        self.manager.add_vehicle_to_hub("Hub1", self.scooter1)

    def test_add_valid_hubs(self):
        self.manager.add_hub("downtown")
        self.manager.add_hub("airport")

        self.assertIn("downtown", self.manager.fleet_hubs)
        self.assertIn("airport", self.manager.fleet_hubs)

    def test_duplicate_vehicle_not_added(self):
        self.manager.add_hub("downtown")

        self.manager.add_vehicle_to_hub("downtown", self.car)
        result = self.manager.add_vehicle_to_hub("downtown", self.car)

        self.assertFalse(result)

    def test_search_by_hub(self):
        self.manager.add_hub("airport")
        self.manager.add_vehicle_to_hub("airport", self.car)

        vehicles = self.manager.search_by_hub("airport")
        self.assertEqual(len(vehicles), 1)

    def test_categorize_by_type(self):
        self.manager.add_hub("downtown")

        self.manager.add_vehicle_to_hub("downtown", self.car)
        self.manager.add_vehicle_to_hub("downtown", self.scooter)

        categories = self.manager.categorize_by_type()

        self.assertEqual(len(categories["Car"]), 3)
        self.assertEqual(len(categories["Scooter"]), 2)

    def test_fleet_analytics(self):
        self.manager.add_hub("airport")

        self.car.status = "On Trip"
        self.scooter.status = "Available"

        self.manager.add_vehicle_to_hub("airport", self.car)
        self.manager.add_vehicle_to_hub("airport", self.scooter)

        summary = self.manager.fleet_analytics()
        self.assertEqual(summary["On Trip"], 2)
        self.assertEqual(summary["Available"], 3)

    def test_sort_by_model(self):
        self.manager.sort_by_model("Hub1")
        models = [v.model for v in self.manager.search_by_hub("Hub1")]
        self.assertEqual(models, sorted(models))

    def test_sort_by_battery(self):
        self.manager.sort_by_battery("Hub1")
        batteries = [v.get_battery_percentage() for v in self.manager.search_by_hub("Hub1")]
        self.assertEqual(batteries, sorted(batteries, reverse=True)) 

    def test_save_and_load_csv(self):
        filename = "test_fleet.csv"

        # Save current fleet to CSV
        self.manager.save_fleet_management_to_csv(filename)

        # Load CSV into a new FleetManager
        new_manager = FleetManager()
        new_manager.load_fleet_management_from_csv(filename)

        # Verify hub exists
        vehicles = new_manager.search_by_hub("Hub1")
        self.assertEqual(len(vehicles), 3)

        # Verify vehicle IDs
        vehicle_ids = [v.vehicle_id for v in vehicles]
        self.assertIn("EC101", vehicle_ids)
        self.assertIn("EC102", vehicle_ids)
        self.assertIn("ES201", vehicle_ids)

        # Clean up test file
        os.remove(filename)

    def test_save_and_load_json(self):
        filename = "test_fleet.json"

        # Save current fleet to JSON
        self.manager.save_fleet_management_to_json(filename)

        # Load JSON into a new FleetManager
        new_manager = FleetManager()
        new_manager.load_fleet_management_from_json(filename)

        # Verify hub exists
        vehicles = new_manager.search_by_hub("Hub1")
        self.assertEqual(len(vehicles), 3)

        # Verify vehicle IDs
        vehicle_ids = [v.vehicle_id for v in vehicles]
        self.assertIn("EC101", vehicle_ids)
        self.assertIn("EC102", vehicle_ids)
        self.assertIn("ES201", vehicle_ids)

        # Clean up test file
        os.remove(filename)

    if __name__ == "__main__":
        unittest.main()

    
