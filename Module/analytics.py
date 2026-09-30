from data import customers, vehicles, jobs, parts
from jobs import find_job

#workshop dashboard
def workshop_dashboard():
    print("\n========== WORKSHOP DASHBOARD ==========")

    total_customers=len(customers)
    total_vehicles=len(vehicles)

    pending=0
    in_progress=0
    completed=0

    revenue=0

    service_count={}

    for job in jobs:

        if job["status"]=="PENDING":
            pending+=1

        elif job["status"]=="IN PROGRESS":
            in_progress+=1

        elif job["status"] in ["COMPLETED","DELIVERED"]:
            completed+=1

        revenue+=job.get("final_bill",0)

        for service in job["services"]:
            name=service["name"]

            if name in service_count:
                service_count[name]+=1
            else:
                service_count[name]=1

    print("\nTotal Customers :",total_customers)
    print("Total Vehicles  :",total_vehicles)
    print("Total Jobs      :",len(jobs))

    print("\nPending Jobs    :",pending)
    print("In Progress     :",in_progress)
    print("Completed Jobs  :",completed)

    print("\nTotal Revenue   :","₹"+str(round(revenue,2)))

    if service_count:

        most_requested=max(
            service_count,
            key=service_count.get
        )

        print(
            "\nMost Requested Service:",
            most_requested
        )

        print(
            "Times Requested:",
            service_count[most_requested]
        )

    print("\n=========================================")

#inventory report
def inventory_report():
    print("\n========== INVENTORY REPORT ==========")

    if not parts:
        print("No parts in inventory.")
        return

    for part in parts:

        print(
            part["id"],
            "|",
            part["name"],
            "| Stock:",
            part["stock"]
        )

        if part["stock"]<=2:
            print("   WARNING: LOW STOCK!")

#search job
def search_job():
    print("\n========== SEARCH JOB ==========")

    job_id=input("Enter Job ID: ").strip().upper()

    job=find_job(job_id)

    if job is None:
        print("Job not found.")
        return

    print("\nJob Found")
    print("-----------------------------")
    print("Job ID :",job["id"])
    print("Date   :",job["date"])
    print("Status :",job["status"])
    print("Customer ID:",job["customer_id"])
    print("Vehicle ID :",job["vehicle_id"])
    print("Subtotal:","₹"+str(job["subtotal"]))

    if job["final_bill"]>0:
        print("Final Bill:","₹"+str(job["final_bill"]))
