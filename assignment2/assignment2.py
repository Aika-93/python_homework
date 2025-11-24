import csv
import os
import custom_module
from datetime import datetime

#Task_2: Read a CSV File
def read_employees():
    myDict = {}
    myList = []
    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    myDict.update({"fields": row})
                else:
                    myList.append(row)
            myDict.update({"rows": myList})
    except Exception as e:
        return f"An error occured {e}"
        sys.exit(1)
    return myDict

employees = read_employees()
print(employees)


#Task_3: Find the Column Index
def column_index(a):
    if a in employees["fields"]:
        return employees["fields"].index(a)
    else:
        return None


employee_id_column = column_index("employee_id")
print(employee_id_column)


#Task_4: Find the Employee First Name
def first_name(row_num):
    column = column_index("first_name")
    return employees["rows"][row_num][column]

f_name = first_name(3)
print(f_name)


#Task_5:Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches


result = employee_find(3)
print(result)


#Task_6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

result = employee_find_2(2)
print(result)


#Task_7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    employees["rows"].sort(key = lambda row: row[column_index("last_name")])
    return employees["rows"]
    

sort_by_last_name()
print(employees["rows"])


#Task_8: Create a dict for an Employee
def employee_dict(row):
    keys = employees["fields"][1:]
    values = row[1:]
    new_dict = dict(zip(keys, values))
    return new_dict


result = employee_dict(['10', 'Kelli', 'Bowman', '+379 (843)240-1818x77648'])
print(result)


#Task_9:  A dict of dicts, for All Employees
def all_employees_dict():
    all_employees = {} 
    for row in employees["rows"]:
        all_employees.update({row[0]: employee_dict(row)})
    return all_employees
        

result = all_employees_dict()
print(result)


#Task_10: Use the os Module
def get_this_value():
    a = os.getenv("THISVALUE")
    return a

result = get_this_value()
print(result)

#Task_11: Creating Your Own Module
def set_that_secret(secret):
    custom_module.set_secret(secret)
    
set_that_secret("Code")
print(custom_module.secret)


#Task_12: Read minutes1.csv and minutes2.csv
def read_minutes():
    def read_csv(file_name):
        results = {"fields": [], "rows": []}
        with open(file_name) as f:
            reader = csv.reader(f)
            results["fields"] = next(reader)
            results["rows"] = [tuple(row) for row in reader]
        return results
    
    minutes1 = read_csv("../csv/minutes1.csv")
    minutes2 = read_csv("../csv/minutes2.csv")
    return minutes1, minutes2


minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)


#Task_13: Create minutes_set
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    new_set = set1 | set2
    return new_set

minutes_set = create_minutes_set()
print(minutes_set)


#Task_14: Convert to datetime
def create_minutes_list():
    newList = list(minutes_set)
    result = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), newList))
    return result

minutes_list = create_minutes_list()
print(minutes_list)


#Task_15: Write Out Sorted List
def write_sorted_list():
    minutes_sort = sorted(minutes_list, key=lambda x: x[1])
    newlist = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_sort))

    with open("./minutes.csv", "w", newline = "") as f:
        writer = csv.writer(f)
        writer.writerow(minutes1["fields"])
        writer.writerows(newlist)
    return newlist

result = write_sorted_list()
print(result)

