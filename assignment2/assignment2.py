
#Task 2: Read CSV file
import csv
import traceback

def read_employees():
    employees_dict = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r") as employees_file:
            reader = csv.reader(employees_file)

            for row_number, row in enumerate(reader):
                if row_number == 0:
                    employees_dict["fields"] = row
                else:
                    rows.append(row)

        employees_dict["rows"] = rows
        return employees_dict

    except Exception as e:
        print(f"Exception type: {type(e).__name__}")

        message = str(e)

        if message:
            print(f"Exception message: {message}")


employees = read_employees()
print(employees)



#Task 3: Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column=column_index("employee_id")
print(employee_id_column)



#Task 4: Find Employee First Name
def first_name(row_number):
    first_name_column=column_index("first_name")
    return employees["rows"][row_number][first_name_column]

#Task 5: Find employee: a function in a function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

#Task 6: Find the employee with a lambda
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

#Task 7: Sort rows by last_name using a lambda
def sort_by_last_name():
    last_name_column=column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]

sort_by_last_name()
print(employees)

#Task 8: Create a dict for an Employee
def employee_dict(row):
    fields = employees["fields"]
    return {fields[i]: row[i] for i in range(len(fields))
            if fields[i] != "employee_id"}

#Task 9: A dict of dicts for all Employees
def all_employees_dict():
    return {row[employee_id_column]: employee_dict(row) for row in employees["rows"]}
print(all_employees_dict())

#Task 10: use the os Module
import os
def get_this_value():
    return os.getenv("THISVALUE")

#Task 11:
import custom_module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("wackadoo")
print(custom_module.secret)

#Task 12:Read minutes1.csv and minutes2.csv
def read_minutes():
    minutes1_dict = {}
    minutes2_dict = {}
    rows1 = []
    rows2 = []

    try:
        with open("../csv/minutes1.csv", "r") as minutes1_file:
            reader1 = csv.reader(minutes1_file)

            for row_number, row in enumerate(reader1):
                if row_number == 0:
                    minutes1_dict["fields"] = row
                else:
                    rows1.append(tuple(row))

        minutes1_dict["rows"] = rows1

        with open("../csv/minutes2.csv", "r") as minutes2_file:
            reader2 = csv.reader(minutes2_file)

            for row_number, row in enumerate(reader2):
                if row_number == 0:
                    minutes2_dict["fields"] = row
                else:
                    rows2.append(tuple(row))

        minutes2_dict["rows"] = rows2

        return minutes1_dict, minutes2_dict

    except Exception as e:
        print(f"Exception type: {type(e).__name__}")

        message = str(e)

        if message:
            print(f"Exception message: {message}")


minutes1, minutes2 = read_minutes()

print(minutes1)
print(minutes2)

#Task 13: Create minutes_set
def create_minutes_set():
    minutes_set = set()
    for row in minutes1["rows"]:
        minutes_set.add(row)
    for row in minutes2["rows"]:
        minutes_set.add(row)
    return minutes_set

minutes_set = create_minutes_set()
print(minutes_set)

#Task 14: Convert to datetime
from datetime import datetime

def create_minutes_list():
    minutes_list = list(minutes_set)

    minutes_list=list(
        map(
            lambda row: (row[0], datetime.strptime(row[1], "%B %d, %Y")),
            minutes_list
        )
)

    return minutes_list

minutes_list=create_minutes_list()
print(minutes_list)

#Task 15: Write out sorted list
def write_sorted_list():
    minutes_list.sort(key=lambda row: row[1])

    converted_list = list(
        map(
            lambda row: (
                row[0],
                datetime.strftime(row[1], "%B %d, %Y")
            ),
            minutes_list
        )
    )

    with open("./minutes.csv", "w", newline="") as minutes_file:
        writer = csv.writer(minutes_file)

        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)

    return converted_list

sorted_minutes = write_sorted_list()
print(sorted_minutes)