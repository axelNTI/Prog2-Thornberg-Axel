import csv

with open("csv/names.csv", "r") as file:
    reader = csv.DictReader(file)
    modified_rows = [
        {k: v for k, v in row.items() if k != "first_name"} for row in reader
    ]

with open("csv/new_names.csv", "w", newline="") as new_file:
    fieldnames = reader.fieldnames
    fieldnames.remove("first_name")
    writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=",")
    writer.writeheader()
    writer.writerows(modified_rows)
