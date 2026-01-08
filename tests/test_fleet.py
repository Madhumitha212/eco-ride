import pytest
import os
from source.vehicle import FleetManager, ElectricCar, ElectricScooter

@pytest.fixture
def setup_manager():
    manager = FleetManager()
    car = ElectricCar("EC101", "Tesla Model 3", 90, 5)
    scooter = ElectricScooter("ES201", "Ather", 70, 85)
    car1 = ElectricCar("EC102", "Nissan Leaf", 60, 4)
    scooter1 = ElectricScooter("ES201", "Ather", 85, 85)
    manager.add_hub("Hub1")
    manager.add_vehicle_to_hub("Hub1", car)
    manager.add_vehicle_to_hub("Hub1", car1)
    manager.add_vehicle_to_hub("Hub1", scooter)
    manager.add_vehicle_to_hub("Hub1", scooter1)
    return manager, car, scooter, car1, scooter1
def test_add_valid_hubs(setup_manager):
    manager, *_ = setup_manager
    manager.add_hub("downtown")
    manager.add_hub("airport")
    assert "downtown" in manager.fleet_hubs
    assert "airport" in manager.fleet_hubs
def test_duplicate_vehicle_not_added(setup_manager):
    manager, car, *_ = setup_manager
    manager.add_hub("downtown")
    manager.add_vehicle_to_hub("downtown", car)
    result = manager.add_vehicle_to_hub("downtown", car)
    assert result is False
def test_search_by_hub(setup_manager):
    manager, car, *_ = setup_manager
    manager.add_hub("airport")
    manager.add_vehicle_to_hub("airport", car)
    vehicles = manager.search_by_hub("airport")
    assert len(vehicles) == 1
def test_categorize_by_type(setup_manager):
    manager, car, scooter, *_ = setup_manager
    manager.add_hub("downtown")
    manager.add_vehicle_to_hub("downtown", car)
    manager.add_vehicle_to_hub("downtown", scooter)
    categories = manager.categorize_by_type()
    assert len(categories["Car"]) == 3
    assert len(categories["Scooter"]) == 2
def test_fleet_analytics(setup_manager):
    manager, car, scooter, *_ = setup_manager
    manager.add_hub("airport")
    car.status = "On Trip"
    scooter.status = "Available"
    manager.add_vehicle_to_hub("airport", car)
    manager.add_vehicle_to_hub("airport", scooter)
    summary = manager.fleet_analytics()
    assert summary["On Trip"] == 2
    assert summary["Available"] == 3
def test_sort_by_model(setup_manager):
    manager, *_ = setup_manager
    manager.sort_by_model("Hub1")
    models = [v.model for v in manager.search_by_hub("Hub1")]
    assert models == sorted(models)
def test_sort_by_battery(setup_manager):
    manager, *_ = setup_manager
    manager.sort_by_battery("Hub1")
    batteries = [v.get_battery_percentage() for v in manager.search_by_hub("Hub1")]
    assert batteries == sorted(batteries, reverse=True)
def test_save_and_load_csv(setup_manager):
    manager, *_ = setup_manager
    filename = "test_fleet.csv"
    manager.save_fleet_management_to_csv(filename)
    new_manager = FleetManager()
    new_manager.load_fleet_management_from_csv(filename)
    vehicles = new_manager.search_by_hub("Hub1")
    assert len(vehicles) == 3
    vehicle_ids = [v.vehicle_id for v in vehicles]
    assert "EC101" in vehicle_ids
    assert "EC102" in vehicle_ids
    assert "ES201" in vehicle_ids 
    os.remove(filename)
def test_save_and_load_json(setup_manager):
    manager, *_ = setup_manager
    filename = "test_fleet.json"
    manager.save_fleet_management_to_json(filename)
    new_manager = FleetManager()
    new_manager.load_fleet_management_from_json(filename)
    vehicles = new_manager.search_by_hub("Hub1")
    assert len(vehicles) == 3
    vehicle_ids = [v.vehicle_id for v in vehicles]
    assert "EC101" in vehicle_ids
    assert "EC102" in vehicle_ids
    assert "ES201" in vehicle_ids
    os.remove(filename)
