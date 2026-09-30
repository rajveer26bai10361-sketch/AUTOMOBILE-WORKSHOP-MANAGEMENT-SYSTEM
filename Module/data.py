import json
import os
from datetime import datetime

#file handling
customer_file="customer.json"
vehicle_file="vehicles.json"
job_file="jobs.json"
part_file="parts.json"

def load_data(filename):
    if os.path.exists(filename):
        try:
            with open(filename,"r") as file:
                return json.load(file)
        except:
            return []
    return []

def save_data(filename,data):
    with open(filename,"w") as file:
        json.dump(data,file,indent=4)

#load existing data when program starts
customers=load_data(customer_file)
vehicles=load_data(vehicle_file)
jobs=load_data(job_file)
parts=load_data(part_file)

#id generation
def generate_id(prefix,data,key):
    if not data:
        return prefix+"101"

    numbers=[]

    for item in data:
        try:
            number=int(item[key][1:])
            numbers.append(number)
        except:
            pass

    if numbers:
        return prefix+str(max(numbers)+1)

    return prefix+"101"

#input validation
def get_phone():
    while True:
        phone=input("enter phone number: ").strip()

        if phone.isdigit() and len(phone)==10:
            return phone

        print("invalid phone number, enter exactly 10 digits")

def get_number(message):
    while True:
        try:
            value=int(input(message))

            if value>=0:
                return value

            print("enter a positive number")

        except ValueError:
            print("invalid input. Enter a number.")
