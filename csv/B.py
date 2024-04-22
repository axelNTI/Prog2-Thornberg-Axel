import csv


def average_grade(grades: list[str]) -> float:
    grade_lookup: dict[str, float] = {
        "A": 20,
        "B": 17.5,
        "C": 15,
        "D": 12.5,
        "E": 10,
        "F": 0,
    }
    return sum(grade_lookup[grade] for grade in grades) / len(grades)


def average(arr: list[int]) -> float:
    return sum(arr) / len(arr)


with open("csv/Klasslista.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file, delimiter=";")
    grades = list(reader)
    print(
        average(
            [
                average_grade([row[key] for row in grades])
                for key in grades[0].keys()
                if key != "Namn"
            ]
        )
    )
