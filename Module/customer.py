from data import customers, customer_file, generate_id, get_phone, save_data

#customer management
def add_customer():
    print("\n========== ADD CUSTOMER ==========")

    name=input("enter customer name: ").strip()

    if not name:
        print("name cannot be empty.")
        return

    phone=get_phone()

    #prevent duplicate phone number
    for customer in customers:
        if customer["phone"]==phone:
            print("a customer with this phone number already exists.")
            print("customer_id:",customer["id"])
            return

    customer_id=generate_id("C",customers,"id")

    customer={
        "id":customer_id,
        "name":name,
        "phone":phone
    }

    customers.append(customer)
    save_data(customer_file,customers)

    print("\nCustomer registered successfully!!")
    print("customer_id:",customer_id)

def search_customer():
    print("\n========== SEARCH CUSTOMER ==========")

    search=input("enter customer id, name or phone: ").strip().lower()
    found=False

    for customer in customers:
        if (search==customer["id"].lower()
            or search==customer["phone"]
            or search in customer["name"].lower()):

            print("\nCustomer Found")
            print("------------------------")
            print("ID    :",customer["id"])
            print("Name  :",customer["name"])
            print("Phone :",customer["phone"])

            found=True

    if not found:
        print("customer not found.")

def view_customer():
    print("\n========== ALL CUSTOMERS ==========")

    if not customers:
        print("No customers registered.")
        return

    for customer in customers:
        print("------------------------")
        print("ID    :",customer["id"])
        print("Name  :",customer["name"])
        print("Phone :",customer["phone"])


#customer menu
def customer_menu():

    while True:

        print("\n========== CUSTOMER MANAGEMENT ==========")
        print("1. Add Customer")
        print("2. Search Customer")
        print("3. View All Customers")
        print("4. Back")

        choice=get_number("Enter choice: ")

        if choice==1:
            add_customer()

        elif choice==2:
            search_customer()

        elif choice==3:
            view_customer()

        elif choice==4:
            break

        else:
            print("Invalid choice.")
