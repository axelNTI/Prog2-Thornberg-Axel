import csv

with open("csv/names.csv", "r") as file:
    reader = csv.DictReader(file)
    remove_jane = [row for row in reader if row["first_name"] != "Jane"]
    modified_rows = [
        {k: v for k, v in row.items() if k != "first_name"} for row in remove_jane
    ]
    for index, row in enumerate(modified_rows):
        row["index"] = index + 1

with open("csv/new_names.csv", "w", newline="") as new_file:
    fieldnames = reader.fieldnames
    fieldnames.remove("first_name")
    fieldnames.append("index")
    writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=",")
    writer.writeheader()
    writer.writerows(modified_rows)
