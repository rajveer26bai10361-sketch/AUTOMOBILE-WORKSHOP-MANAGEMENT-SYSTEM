from data import customers, vehicles, vehicle_file, generate_id, get_number, save_data

#vehicle management
def add_vehicle():
    print("\n========== ADD VEHICLE ==========")

    customer_id=input("Enter Customer ID: ").strip().upper()

    customer=None

    for c in customers:
        if c["id"]==customer_id:
            customer=c
            break

    if customer is None:
        print("Customer not found.")
        return

    registration=input("Enter registration number: ").strip().upper()

    for vehicle in vehicles:
        if vehicle["registration"]==registration:
            print("A vehicle with this registration already exists.")
            return

    brand=input("Enter vehicle brand: ").strip()
    model=input("Enter vehicle model: ").strip()
    year=get_number("Enter manufacturing year: ")

    fuel=input("Enter fuel type (Petrol/Diesel/CNG/EV): ").strip()

    vehicle_id=generate_id("V",vehicles,"id")

    vehicle={
        "id":vehicle_id,
        "customer_id":customer_id,
        "brand":brand,
        "model":model,
        "registration":registration,
        "year":year,
        "fuel":fuel
    }

    vehicles.append(vehicle)
    save_data(vehicle_file,vehicles)

    print("\nVehicle registered successfully!")
    print("Vehicle ID:",vehicle_id)

def search_vehicle():
    print("\n========== SEARCH VEHICLE ==========")

    search=input(
        "Enter Vehicle ID, registration number or Customer ID: "
    ).strip().upper()

    found=False

    for vehicle in vehicles:
        if (vehicle["id"]==search
            or vehicle["registration"]==search
            or vehicle["customer_id"]==search):

            print("\nVehicle Found")
            print("------------------------")
            print("Vehicle ID :",vehicle["id"])
            print("Customer ID:",vehicle["customer_id"])
            print("Brand      :",vehicle["brand"])
            print("Model      :",vehicle["model"])
            print("Registration:",vehicle["registration"])
            print("Year       :",vehicle["year"])
            print("Fuel       :",vehicle["fuel"])

            found=True

    if not found:
        print("Vehicle not found.")

def view_vehicles():
    print("\n========== ALL VEHICLES ==========")

    if not vehicles:
        print("No vehicles registered.")
        return

    for vehicle in vehicles:
        print("------------------------")
        print("Vehicle ID :",vehicle["id"])
        print("Customer ID:",vehicle["customer_id"])
        print("Vehicle    :",vehicle["brand"],vehicle["model"])
        print("Registration:",vehicle["registration"])
        print("Fuel       :",vehicle["fuel"])


#vehicle menu
def vehicle_menu():

    while True:

        print("\n========== VEHICLE MANAGEMENT ==========")
        print("1. Add Vehicle")
        print("2. Search Vehicle")
        print("3. View All Vehicles")
        print("4. Back")

        choice=get_number("Enter choice: ")

        if choice==1:
            add_vehicle()

        elif choice==2:
            search_vehicle()

        elif choice==3:
            view_vehicles()

        elif choice==4:
            break

        else:
            print("Invalid choice.")
