from vehicle import*
fm = FleetManager()
fm.load_fleet_management_from_csv()

def main():
    print("Welcome to Eco-Ride urban mobility system")
    
    fm.add_hub("Downtown")
    fm.add_hub("Airport")

    # Add vehicles
    car = ElectricCar("EC601", "Tesla Model 3", 90, 5)
    scooter = ElectricScooter("ES603", "Ather 450X", 80, 85)

    fm.add_vehicle_to_hub("Downtown", car)
    fm.add_vehicle_to_hub("Airport", scooter)

    # Save before exit (UC-13)
    fm.save_fleet_management_to_csv()

    print("Fleet data saved successfully.")

if __name__ == "__main__":
    main()