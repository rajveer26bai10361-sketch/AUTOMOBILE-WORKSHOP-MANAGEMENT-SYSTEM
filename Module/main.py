from data import get_number
from customer import customer_menu
from vehicle import vehicle_menu
from services import display_services, display_parts, initialize_parts
from jobs import (
    create_job_card,
    view_job_card,
    update_job_status,
    generate_bill,
    view_service_history
)
from analytics import workshop_dashboard, inventory_report, search_job

#main menu
def main():

    initialize_parts()

    while True:

        print("\n")
        print("╔════════════════════════════════════════╗")
        print("║      AUTOMOBILE WORKSHOP MANAGEMENT    ║")
        print("║                SYSTEM                  ║")
        print("╚════════════════════════════════════════╝")

        print("\n1. Customer Management")
        print("2. Vehicle Management")
        print("3. View Service Catalogue")
        print("4. View Parts Inventory")
        print("5. Create Job Card")
        print("6. View Job Card")
        print("7. Update Job Status")
        print("8. Generate Bill")
        print("9. Service History")
        print("10. Workshop Dashboard")
        print("11. Inventory Report")
        print("12. Search Job")
        print("13. Exit")

        choice=get_number("\nEnter your choice: ")

        if choice==1:
            customer_menu()

        elif choice==2:
            vehicle_menu()

        elif choice==3:
            display_services()

        elif choice==4:
            display_parts()

        elif choice==5:
            create_job_card()

        elif choice==6:
            view_job_card()

        elif choice==7:
            update_job_status()

        elif choice==8:
            generate_bill()

        elif choice==9:
            view_service_history()

        elif choice==10:
            workshop_dashboard()

        elif choice==11:
            inventory_report()

        elif choice==12:
            search_job()

        elif choice==13:
            print("\nThank you for using the Automobile Workshop")
            print("Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


#program start
if __name__=="__main__":
    main()
