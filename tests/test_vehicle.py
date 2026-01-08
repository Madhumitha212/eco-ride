import sys 
import os 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from source.vehicle import Vehicle, ElectricCar,ElectricScooter
import pytest

@pytest.fixture
def car():
  return ElectricCar("EC101", "Tesla Model 3", 80, 5)
@pytest.fixture
def scooter():
  return ElectricScooter("ES201", "Ather", 80, 85)
def test_electric_car_initialization(car):
    assert car.vehicle_id == "EC101"
    assert car.model == "Tesla Model 3"
    assert car.get_battery_percentage() == 80
    assert car.seating_capacity == 5
def test_electric_scooter_initialization(scooter):
    assert scooter.vehicle_id == "ES201"
    assert scooter.model == "Ather"
    assert scooter.get_battery_percentage() == 80
    assert scooter.max_speed_limit == 85
def test_trip_cost(car, scooter):
    assert car.calculate_trip_cost(10) == 5.0 + 0.5 * 10 # 10 km
    assert scooter.calculate_trip_cost(10) == 1.0 + 0.15 * 10
def test_vehicle_cannot_be_instantiated():
    with pytest.raises(TypeError):
       Vehicle(1, "Base", 50)
def test_car_is_vehicle(car):
    assert isinstance(car, Vehicle)