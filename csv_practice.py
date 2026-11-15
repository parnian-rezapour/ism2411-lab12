# Reflection 1 - Python vs. Excel
# Python makes it easier to repeat the same cleaning and reporting steps
# automatically instead of doing them manually each time in Excel.
# Excel is still easier when I want to quickly view, edit, or explore data.

# Reflection 2 - Append-mode log
# A real estate company could use a log to track daily rent collections
# with the date and total amount received.
# Append mode keeps each new entry without deleting previous records,
# making it easier to review the history.
 
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

# Exercise 4 - Compute totals
total_revenue = 0

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")

#Exercise 5 - Filter and write
CLEANED_FILE = "data/cleaned.csv"
high_value = []
rows_read = 0

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        rows_read += 1
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity

        if total > 100:
            high_value.append([product, f"{price:.2f}", quantity, f"{total:.2f}"])

with open(CLEANED_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    writer.writerows(high_value)

print(f"Wrote {len(high_value)} of {rows_read} rows to {CLEANED_FILE}.")

# Exercise 6 - Read with csv.DictReader
# csv.reader is useful when the column order is known and won't change.
# DictReader is better when I want to access columns by name, even if their order changes.

dict_total = 0

with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"DictReader total revenue: ${dict_total:.2f}")

# Exercise 7 - Sales summary by product
summary = {}

with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        product = row["product"]
        total = float(row["price"]) * int(row["quantity"])
        summary[product] = summary.get(product, 0) + total

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

# Exercise 8 - Append-mode log
from datetime import datetime

LOG_FILE = "data/run_log.txt"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(LOG_FILE, "a") as f:
    f.write(f"{timestamp} | Total revenue: ${total_revenue:.2f}\n")

print(f"Added a log entry to {LOG_FILE}.")





