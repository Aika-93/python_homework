#Task_3: List Comprehensions Practice
import csv
try:
    with open ("../csv/employees.csv", "r", newline='') as file:
        reader = csv.reader(file)
        data_list = list(reader)
        first_name = x[1]
        last_name = x[2]
        employee_names = [row[1] + " " + row[2] for row in data_list if x[1] != "first_name"]
        names_with_e = [name for name in employee_names if "e" in name.lower()]
        print(employee_names) 
        print(names_with_e)
except Exception as e:
    print(f"An error occurred: {e}")