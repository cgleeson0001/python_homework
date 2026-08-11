#TASK 1: INTRO TO PANDAS
import pandas as pd

#create df from a dictionary
employee_data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

task1_data_frame = pd.DataFrame(employee_data)

print(task1_data_frame)

#add salary
task1_with_salary = task1_data_frame.copy()

task1_with_salary["Salary"] = [70000, 80000, 90000]

print(task1_with_salary)

#modify column
task1_older=task1_with_salary.copy()

task1_older["Age"] = task1_older["Age"] + 1

print(task1_older)

#save df as csv
task1_older.to_csv("employees.csv", index=False)

#TASK 2:LOADING DATA

#read employees.csv
task2_employees = pd.read_csv("employees.csv")

print(task2_employees)

#read json file
json_employees = pd.read_json("additional_employees.json")

print(json_employees)

#combine dfs
more_employees = pd.concat(
    [task2_employees, json_employees],
    ignore_index=True
)

print(more_employees)

#TASK 3: DATA INSPECTION

#head
first_three=more_employees.head(3)

print(first_three)

#tail
last_two=more_employees.tail(2)
print(last_two)

#shape
employee_shape=more_employees.shape

print(employee_shape)

#df summary
more_employees.info()

#TASK 4: DIRTY DATA
dirty_data = pd.read_csv("dirty_data.csv")

print(dirty_data)

clean_data = dirty_data.copy()

#drop duplicates
clean_data = clean_data.drop_duplicates()

print(clean_data)

#fix age datatype and handle missing values
clean_data["Age"] = pd.to_numeric(
    clean_data["Age"],
    errors="coerce"
)

print(clean_data)

#clean salary
clean_data["Salary"]=clean_data["Salary"].replace(
    ["unknown", "n/a"],
    pd.NA
)

print(clean_data)

clean_data["Salary"]=pd.to_numeric(
           clean_data["Salary"],
             errors="coerce"
)

print(clean_data)

#fill missing values

clean_data["Age"] = clean_data["Age"].fillna(
    clean_data["Age"].mean()
)

clean_data["Salary"] = clean_data["Salary"].fillna(
    clean_data["Salary"].median()
)

print(clean_data)

#datetime conversion
clean_data["Hire Date"] = pd.to_datetime(
    clean_data["Hire Date"],
    format="mixed"
)

print(clean_data)

#clean name and dept

clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = (
    clean_data["Department"]
    .str.strip()
    .str.upper()
)

print(clean_data)