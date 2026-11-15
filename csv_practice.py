import csv

# Exercise 1 - Set up the sales CSV file
SALES_FILE = "data/sales.csv"

# Exercise 2 - Read and print raw rows
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Exercise 3 - Skip the header
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)
