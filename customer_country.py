import csv

customers = open("customers.csv", "r")
customer_file = csv.reader(customers, delimiter=",")
next(customer_file)

with open("customer_country.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["FirstName", "LastName", "Country"])
    for record in customer_file:
        writer.writerow([record[1], record[2], record[4]])

file.close()
customers.close()
