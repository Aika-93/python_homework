#Task_3: List Comprehensions Practice
import csv

with open ("../csv/employees.csv", "r") as file:
    reader = csv.reader(file)
    data_list = list(reader)
    employee_names = [x[1] + " " + x[2] for x in data_list if x[1] != "first_name"]
    names_with_e = [name for name in employee_names if "e" in name.lower()]
    print(employee_names) 
    print(names_with_e)
