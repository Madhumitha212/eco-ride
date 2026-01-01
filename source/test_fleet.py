import unittest
from vehicle import*

class TestFleetManager(unittest.TestCase):

    def setUp(self):
        self.car = ElectricCar("EC101", "Tesla Model 3", 80, 5)
        self.scooter = ElectricScooter("ES201", "Ather", 80, 85)

    def test_electric_car_initialization(self): 
        self.assertEqual(self.car.vehicle_id, "EC101")
        self.assertEqual(self.car.model, "Tesla Model 3")
        self.assertEqual(self.car.get_battery_percentage(), 80)
        self.assertEqual(self.car.seating_capacity, 5)

    def test_electric_scooter_initialization(self):

        self.assertEqual(self.scooter.vehicle_id, "ES201")
        self.assertEqual(self.scooter.model, "Ather")
        self.assertEqual(self.scooter.get_battery_percentage(), 80)
        self.assertEqual(self.scooter.max_speed_limit, 85)

    def test_trip_cost(self):
        self.assertEqual(self.car.calculate_trip_cost(10), 5.0 + 0.5 * 10)  # 10 km
        self.assertEqual(self.scooter.calculate_trip_cost(10), 1.0 + 0.15 * 10)

    def test_vehicle_cannot_be_instantiated(self):
        with self.assertRaises(TypeError):
            Vehicle(1, "Base", 50)

    def test_car_is_vehicle(self):
        self.assertIsInstance(self.car, Vehicle)

if __name__ == "__main__":
    unittest.main()