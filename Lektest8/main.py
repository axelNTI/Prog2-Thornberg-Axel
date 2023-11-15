import numpy

lookup_dict = {"F": 0, "E": 10, "D": 12.5, "C": 15, "B": 17.5, "A": 20}

while True:
    try:
        print("Calculate your average grade.")
        grades = numpy.array(
            str(
                input(
                    "Enter your grades by letter followed by points, each pair is to be seperated by a space. Such as this example: A 100 C 150 E 50\n"
                )
            )
            .upper()
            .split(" ")
        ).reshape(-1, 2)
        grades = [list(i) for i in grades]
        numerator = sum(list(map(lambda x: lookup_dict[x[0]] * int(x[1]), grades)))
        denomenator = sum([int(i[1]) for i in grades])
        print(f"Your average grade is { numerator / denomenator }\n")
    except:
        print("One of your grades is not valid.\n")
