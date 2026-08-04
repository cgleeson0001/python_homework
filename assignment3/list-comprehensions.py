import csv

#read employee.csv
employees=[]
with open("../csv/employees.csv", newline="") as csvfile:
    reader=csv.reader(csvfile)

    for row in reader:
        employees.append(row)

#create list
employee_names=[
    f"{row[1]} {row[2]}"
    for row in employees[1:]
]
print(employee_names)

#create list only names with letter "e"
names_with_e=[
    name
    for name in employee_names
    if "e" in name
]
print(names_with_e)