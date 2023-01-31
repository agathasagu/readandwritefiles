import csv

employees = open("EmployeePay.csv", "r")

employee_details = csv.reader(employees, delimiter=",")

next(employee_details)

for record in employee_details:
    print("ID:", record[0])
    print("First Name:", record[1])
    print("Last Name:", record[2])
    print("Salary:", record[3])
    print("Bonus:", record[4])
    print("------------------------------")
    print()

employees.close()
