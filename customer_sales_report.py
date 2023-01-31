import csv

sales = open("sales.csv", "r")
customer_sales = csv.reader(sales, delimiter=",")
next(customer_sales)

with open("salesreport.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Customer ID", "Total"])
    totalsales = {}
    for record in customer_sales:
        customerid = record[0]
        total = float(record[3]) + float(record[4]) + float(record[5])

        if customerid in totalsales:
            totalsales[customerid] += total
        else:
            totalsales[customerid] = total

    # print(totalsales)
    for key, value in totalsales.items():
        value = round(value, 2)
        writer.writerow([key, value])


file.close()
sales.close()
