from data import parts, part_file, save_data, get_number

#service catalogue
services={
    1:("Car Wash",300),
    2:("Oil Change",800),
    3:("Wheel Alignment",600),
    4:("Wheel Balancing",500),
    5:("Brake Inspection",400),
    6:("AC Service",1200),
    7:("Battery Check",200),
    8:("Full Car Service",2500)
}

def display_services():
    print("\n========== SERVICE CATALOGUE ==========")

    for number,service in services.items():
        print(f"{number}. {service[0]:25} ₹{service[1]}")

def select_services():
    display_services()

    selected=[]

    while True:
        choice=get_number("Select service (0 to finish): ")

        if choice==0:
            break

        if choice not in services:
            print("Invalid service.")
            continue

        service_name,price=services[choice]

        already_added=False

        for service in selected:
            if service["name"]==service_name:
                already_added=True
                break

        if already_added:
            print("Service already added.")
            continue

        selected.append({
            "name":service_name,
            "price":price
        })

        print(service_name,"added.")

    return selected

#parts inventory
def initialize_parts():
    if parts:
        return

    default_parts=[
        {"id":"P101","name":"Front Bumper","price":8000,"stock":5},
        {"id":"P102","name":"Rear Bumper","price":8000,"stock":5},
        {"id":"P103","name":"Side Mirror","price":2500,"stock":8},
        {"id":"P104","name":"Headlight","price":5000,"stock":6},
        {"id":"P105","name":"Tail Light","price":3500,"stock":6},
        {"id":"P106","name":"Bonnet","price":9000,"stock":3},
        {"id":"P107","name":"Door","price":12000,"stock":4},
        {"id":"P108","name":"Windshield","price":7000,"stock":5}
    ]

    parts.extend(default_parts)
    save_data(part_file,parts)

def display_parts():
    print("\n========== PARTS INVENTORY ==========")

    if not parts:
        print("No parts available.")
        return

    for part in parts:
        print(
            f"{part['id']} | "
            f"{part['name']:18} | "
            f"₹{part['price']:6} | "
            f"Stock: {part['stock']}"
        )

def select_parts():
    display_parts()

    selected=[]

    while True:
        part_id=input(
            "\nEnter Part ID (0 to finish): "
        ).strip().upper()

        if part_id=="0":
            break

        part=None

        for p in parts:
            if p["id"]==part_id:
                part=p
                break

        if part is None:
            print("Part not found.")
            continue

        quantity=get_number("Enter quantity: ")

        if quantity==0:
            print("Quantity must be greater than zero.")
            continue

        already_selected=0

        for item in selected:
            if item["id"]==part["id"]:
                already_selected=item["quantity"]
                break

        if quantity+already_selected>part["stock"]:
            print("Not enough stock available.")
            continue

        if already_selected>0:
            for item in selected:
                if item["id"]==part["id"]:
                    item["quantity"]+=quantity
                    break
        else:
            selected.append({
                "id":part["id"],
                "name":part["name"],
                "price":part["price"],
                "quantity":quantity
            })

        print(part["name"],"added.")

    return selected
