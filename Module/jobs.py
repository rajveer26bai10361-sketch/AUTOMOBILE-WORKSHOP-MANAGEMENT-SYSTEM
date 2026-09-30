from datetime import datetime
from data import customers, vehicles, jobs, parts, job_file, part_file, generate_id, get_number, save_data
from services import select_services, select_parts

#job card
def create_job_card():
    print("\n========== CREATE JOB CARD ==========")

    customer_id=input("Enter Customer ID: ").strip().upper()

    customer=None

    for c in customers:
        if c["id"]==customer_id:
            customer=c
            break

    if customer is None:
        print("Customer not found.")
        return

    customer_vehicles=[]

    for vehicle in vehicles:
        if vehicle["customer_id"]==customer_id:
            customer_vehicles.append(vehicle)

    if not customer_vehicles:
        print("This customer has no registered vehicles.")
        return

    print("\nCustomer Vehicles:")

    for vehicle in customer_vehicles:
        print(
            vehicle["id"],
            "-",
            vehicle["brand"],
            vehicle["model"],
            "-",
            vehicle["registration"]
        )

    vehicle_id=input("Enter Vehicle ID: ").strip().upper()

    vehicle=None

    for v in customer_vehicles:
        if v["id"]==vehicle_id:
            vehicle=v
            break

    if vehicle is None:
        print("Vehicle not found.")
        return

    print("\nSelect Services")
    selected_services=select_services()

    print("\nSelect Exterior Parts")
    selected_parts=select_parts()

    if not selected_services and not selected_parts:
        print("You must select at least one service or part.")
        return

    labour=get_number("\nEnter labour charges: ₹")

    service_total=sum(
        service["price"] for service in selected_services
    )

    parts_total=sum(
        part["price"]*part["quantity"]
        for part in selected_parts
    )

    subtotal=service_total+parts_total+labour

    job_id=generate_id("J",jobs,"id")

    job={
        "id":job_id,
        "customer_id":customer_id,
        "vehicle_id":vehicle_id,
        "date":datetime.now().strftime("%d-%m-%Y"),
        "services":selected_services,
        "parts":selected_parts,
        "labour":labour,
        "service_total":service_total,
        "parts_total":parts_total,
        "subtotal":subtotal,
        "status":"PENDING",
        "final_bill":0
    }

    jobs.append(job)

    #reduce inventory
    for selected in selected_parts:
        for part in parts:
            if part["id"]==selected["id"]:
                part["stock"]-=selected["quantity"]
                break

    save_data(job_file,jobs)
    save_data(part_file,parts)

    print("\nJob Card created successfully!")
    print("Job ID:",job_id)
    print("Estimated cost:","₹"+str(subtotal))

#view job card
def find_job(job_id):
    for job in jobs:
        if job["id"]==job_id:
            return job

    return None

def view_job_card():
    print("\n========== VIEW JOB CARD ==========")

    job_id=input("Enter Job ID: ").strip().upper()

    job=find_job(job_id)

    if job is None:
        print("Job not found.")
        return

    customer=None
    vehicle=None

    for c in customers:
        if c["id"]==job["customer_id"]:
            customer=c
            break

    for v in vehicles:
        if v["id"]==job["vehicle_id"]:
            vehicle=v
            break

    print("\n======================================")
    print("             JOB CARD")
    print("======================================")

    print("Job ID       :",job["id"])
    print("Date         :",job["date"])

    if customer:
        print("Customer     :",customer["name"])
        print("Phone        :",customer["phone"])

    if vehicle:
        print("Vehicle      :",vehicle["brand"],vehicle["model"])
        print("Registration :",vehicle["registration"])

    print("\nServices:")

    if job["services"]:
        for service in job["services"]:
            print(
                "-",
                service["name"],
                "₹"+str(service["price"])
            )
    else:
        print("- None")

    print("\nParts:")

    if job["parts"]:
        for part in job["parts"]:
            print(
                "-",
                part["name"],
                "x",
                part["quantity"],
                "₹"+str(part["price"]*part["quantity"])
            )
    else:
        print("- None")

    print("\nService Cost :", "₹"+str(job["service_total"]))
    print("Parts Cost   :", "₹"+str(job["parts_total"]))
    print("Labour       :", "₹"+str(job["labour"]))
    print("Subtotal     :", "₹"+str(job["subtotal"]))
    print("Status       :",job["status"])

    print("======================================")

#update job status
def update_job_status():
    print("\n========== UPDATE JOB STATUS ==========")

    job_id=input("Enter Job ID: ").strip().upper()

    job=find_job(job_id)

    if job is None:
        print("Job not found.")
        return

    print("\nCurrent Status:",job["status"])

    print("\n1. PENDING")
    print("2. IN PROGRESS")
    print("3. COMPLETED")
    print("4. DELIVERED")

    choice=get_number("Choose new status: ")

    statuses={
        1:"PENDING",
        2:"IN PROGRESS",
        3:"COMPLETED",
        4:"DELIVERED"
    }

    if choice not in statuses:
        print("Invalid status.")
        return

    new_status=statuses[choice]

    order={
        "PENDING":1,
        "IN PROGRESS":2,
        "COMPLETED":3,
        "DELIVERED":4
    }

    if order[new_status]<order[job["status"]]:
        print("Cannot move job backwards in status.")
        return

    if order[new_status]>order[job["status"]]+1:
        print("You cannot skip a status.")
        return

    if new_status==job["status"]:
        print("Job is already in this status.")
        return

    job["status"]=new_status

    save_data(job_file,jobs)

    print("Status updated successfully.")

#bill generation
def generate_bill():
    print("\n========== GENERATE BILL ==========")

    job_id=input("Enter Job ID: ").strip().upper()

    job=find_job(job_id)

    if job is None:
        print("Job not found.")
        return

    if job["status"] not in ["COMPLETED","DELIVERED"]:
        print("Bill can only be generated for a completed job.")
        return

    subtotal=job["subtotal"]

    gst=subtotal*0.18
    total=subtotal+gst

    job["gst"]=round(gst,2)
    job["final_bill"]=round(total,2)

    save_data(job_file,jobs)

    customer=None
    vehicle=None

    for c in customers:
        if c["id"]==job["customer_id"]:
            customer=c
            break

    for v in vehicles:
        if v["id"]==job["vehicle_id"]:
            vehicle=v
            break

    print("\n======================================")
    print("              INVOICE")
    print("======================================")

    print("Job ID:",job["id"])
    print("Date  :",job["date"])

    if customer:
        print("Customer:",customer["name"])

    if vehicle:
        print("Vehicle :",vehicle["brand"],vehicle["model"])
        print("Number  :",vehicle["registration"])

    print("\nServices:")

    for service in job["services"]:
        print(
            service["name"],
            "₹"+str(service["price"])
        )

    print("\nParts:")

    for part in job["parts"]:
        cost=part["price"]*part["quantity"]

        print(
            part["name"],
            "x",
            part["quantity"],
            "₹"+str(cost)
        )

    print("\nService Cost :", "₹"+str(job["service_total"]))
    print("Parts Cost   :", "₹"+str(job["parts_total"]))
    print("Labour       :", "₹"+str(job["labour"]))
    print("--------------------------------------")
    print("Subtotal     :", "₹"+str(subtotal))
    print("GST (18%)    :", "₹"+str(round(gst,2)))
    print("--------------------------------------")
    print("TOTAL        :", "₹"+str(round(total,2)))
    print("======================================")

#service history
def view_service_history():
    print("\n========== SERVICE HISTORY ==========")

    search=input(
        "Enter Customer ID or Vehicle ID: "
    ).strip().upper()

    found=False

    for job in jobs:
        if (job["customer_id"]==search
            or job["vehicle_id"]==search):

            found=True

            print("\n------------------------------")
            print("Job ID :",job["id"])
            print("Date   :",job["date"])
            print("Status :",job["status"])

            if job["final_bill"]>0:
                print("Amount :","₹"+str(job["final_bill"]))
            else:
                print("Amount :","₹"+str(job["subtotal"]))

            print("Services:")

            for service in job["services"]:
                print("-",service["name"])

    if not found:
        print("No service history found.")
