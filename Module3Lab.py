# Darrick Sandifer Module 3 Lab
# This program defines a Vehicle class and an Automobile subclass.
# It prompts the user for vehicle details, creates an Automobile object and displays the information.
# Module3Lab.py




class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof_type):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof_type = roof_type

def main():
    vehicle_type = "Car"
    year = input("Enter vehicle year: ")
    make = input("Enter vehicle make: ")
    model = input("Enter vehicle model: ")
    doors = input("Enter number of doors (2 or 4): ")
    roof_type = input("Enter roof type (solid or sunroof): ")

    car = Automobile(vehicle_type, year, make, model, doors, roof_type)
    
    print(f"Vehicle Type: {car.vehicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Doors: {car.doors}")
    print(f"Roof Type: {car.roof_type}")

if __name__ == "__main__":
    main()