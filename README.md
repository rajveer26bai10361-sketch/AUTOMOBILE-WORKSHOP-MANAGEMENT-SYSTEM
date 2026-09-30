#  Automobile Workshop Management System

A **Python-based Automobile Workshop Management System** designed to manage customers, vehicles, services, spare parts, job cards, billing, service history, and workshop reports.

The system uses **JSON files for data storage**, making it simple, lightweight, and easy to run without requiring a database.

---

##  Features

###  Customer Management

* Add new customers
* Generate unique Customer IDs
* Validate 10-digit phone numbers
* Prevent duplicate customers using phone numbers
* Search customers by:

  * Customer ID
  * Name
  * Phone number
* View all registered customers

###  Vehicle Management

* Register vehicles under existing customers
* Generate unique Vehicle IDs
* Store:

  * Brand
  * Model
  * Registration number
  * Manufacturing year
  * Fuel type
* Prevent duplicate registration numbers
* Search vehicles by Vehicle ID, registration number, or Customer ID
* View all registered vehicles

###  Service Catalogue

The system provides a predefined service catalogue:

| Service          | Price |
| ---------------- | ----: |
| Car Wash         |  ₹300 |
| Oil Change       |  ₹800 |
| Wheel Alignment  |  ₹600 |
| Wheel Balancing  |  ₹500 |
| Brake Inspection |  ₹400 |
| AC Service       | ₹1200 |
| Battery Check    |  ₹200 |
| Full Car Service | ₹2500 |

Users can select multiple services while creating a job card.

### Parts Inventory

The system maintains an inventory of automobile parts including:

* Front Bumper
* Rear Bumper
* Side Mirror
* Headlight
* Tail Light
* Bonnet
* Door
* Windshield

Each part contains:

* Part ID
* Part name
* Price
* Available stock

The inventory is automatically reduced when parts are used in a job.

###  Job Card Management

A job card can contain:

* Customer details
* Vehicle details
* Selected services
* Required parts
* Labour charges
* Service cost
* Parts cost
* Subtotal
* Job status

Each job receives a unique Job ID.

###  Job Status Management

Jobs move through the following stages:

```text
PENDING
   ↓
IN PROGRESS
   ↓
COMPLETED
   ↓
DELIVERED
```

The system prevents:

* Moving a job backwards
* Skipping a status

###  Billing System

Bills can be generated after a job reaches **COMPLETED** or **DELIVERED** status.

The system calculates:

```text
Subtotal
+ GST (18%)
----------------
Final Bill
```

The generated bill includes service costs, parts costs, labour charges, GST, and the final total.

###  Service History

Service history can be searched using:

* Customer ID
* Vehicle ID

It displays previous job cards, dates, statuses, services, and billing amounts.

###  Workshop Dashboard

The dashboard provides information such as:

* Total customers
* Total vehicles
* Total jobs
* Pending jobs
* Jobs in progress
* Completed jobs
* Total revenue
* Most requested service

###  Inventory Report

The inventory report displays current stock levels and gives a **LOW STOCK warning** when a part has 2 or fewer units remaining.

###  Job Search

Jobs can be searched using their Job ID to quickly view:

* Job details
* Date
* Status
* Customer ID
* Vehicle ID
* Subtotal
* Final bill

---

##  Technologies Used

* **Python**
* **JSON**
* **File Handling**
* **Functions**
* **Lists**
* **Dictionaries**
* **Loops**
* **Conditional Statements**
* **Input Validation**
* **Exception Handling**
* **Date and Time**

The program uses Python's built-in `json`, `os`, and `datetime` modules.

---

##  Data Storage

The application stores its data in four JSON files:

```text
customer.json
vehicles.json
jobs.json
parts.json
```

These files are automatically loaded when the program starts and updated whenever data changes.

---

##  Project Structure

```text
Automobile-Workshop-Management-System/
│
├── AUTOMOBILE WORKSHOP MANAGEMENT SYSTEM.py
├── customer.json
├── vehicles.json
├── jobs.json
├── parts.json
└── README.md
```

> The JSON files are created/updated by the program as data is stored.

---

## ▶️ How to Run

### 1. Install Python

Make sure Python 3.x is installed on your system.

Check your Python version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone <repository-url>
```

### 3. Open the Project Folder

```bash
cd Automobile-Workshop-Management-System
```

### 4. Run the Program

```bash
python "AUTOMOBILE WORKSHOP MANAGEMENT SYSTEM.py"
```

---

##  Main Menu

After starting the program, the following menu is displayed:

```text
1. Customer Management
2. Vehicle Management
3. View Service Catalogue
4. View Parts Inventory
5. Create Job Card
6. View Job Card
7. Update Job Status
8. Generate Bill
9. Service History
10. Workshop Dashboard
11. Inventory Report
12. Search Job
13. Exit
```

---

##  Input Validation

The system includes basic input validation.

For example:

* Phone numbers must contain exactly 10 digits.
* Negative numbers are rejected.
* Invalid numeric inputs are handled.
* Duplicate customer phone numbers are prevented.
* Duplicate vehicle registration numbers are prevented.
* Invalid service and part IDs are rejected.
* Parts cannot be selected beyond available stock.

The phone-number validation and numeric input validation are implemented through dedicated functions.

---

##  Billing Calculation

The billing system calculates GST at **18%**.

```text
GST = Subtotal × 0.18

Final Bill = Subtotal + GST
```

The bill is only generated when the job status is `COMPLETED` or `DELIVERED`.

---

##  Workflow

The general workflow of the system is:

```text
Add Customer
      ↓
Register Vehicle
      ↓
Create Job Card
      ↓
Select Services & Parts
      ↓
Add Labour Charges
      ↓
Job Status: PENDING
      ↓
IN PROGRESS
      ↓
COMPLETED
      ↓
Generate Bill
      ↓
DELIVERED
```

---

##  Project Objective

The main objective of this project is to create a simple computerized system for managing the daily operations of an automobile workshop.

It reduces the need for manual record keeping and provides a structured way to manage:

* Customer records
* Vehicle records
* Service requests
* Spare parts
* Job cards
* Billing
* Service history
* Workshop statistics
* Inventory

---

##  Future Improvements

The project can be extended by adding:

* User login and authentication
* Admin and mechanic accounts
* Graphical User Interface (GUI)
* Database integration using MySQL/SQLite
* Online appointment booking
* PDF invoice generation
* Customer notifications
* Mechanic assignment
* Service reminders
* Advanced sales and revenue reports
* Backup and restore functionality

---

##  Author

**Rajveer Tyagi**

B.Tech CSE / AI-ML
VIT Bhopal University

---

##  License

This project was developed as an academic project for learning and demonstrating Python programming, file handling, data structures, and basic software management concepts.
