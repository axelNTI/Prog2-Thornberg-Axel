import pickle


try:
    # VSCode filepath
    with open("Lektest10/number.pkl", "rb") as file:
        number = pickle.load(file)
    print(f"The Highest submitted number is {number}")
    empty_file = False
except Exception:
    print("No previously submitted number")
    empty_file = True

while True:
    try:
        new_number = float(input("Input a number\n"))
        if empty_file:
            print("Your number is the new highscore")
            # VSCode filepath
            with open("Lektest10/number.pkl", "wb") as file:
                pickle.dump(new_number, file)
            break
        if new_number > number:
            print("Your number is the new highscore")
            # VSCode filepath
            with open("Lektest10/number.pkl", "wb") as file:
                pickle.dump(new_number, file)
            break
        print("Your number is lower than the highscore")
        break

    except Exception:
        print("Not a number, try again")
