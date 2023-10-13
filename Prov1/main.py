import difflib


class Bike:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


dict_of_operations = {
    "Add": "add_bike(list_of_bikes)",
    "Show": "show_bikes(list_of_bikes)",
    "Remove": "remove_bike(list_of_bikes)",
    "Most Expensive": "show_most_expensive_bike_price(list_of_bikes)",
}
list_of_bikes = []


def add_bike(list_of_bikes) -> list:
    name = input("Enter the name for the new bike:\n")
    while True:
        try:
            price = int(input("Enter the price of the new bike (kr):\n"))
            break
        except ValueError:
            print("That was not a number. Try again")
        except:
            pass
    list_of_bikes.append(Bike(name, price))
    return sorted(list_of_bikes, key=lambda x: x.price)


def show_bikes(list_of_bikes) -> None:
    try:
        if not len(list_of_bikes):
            print("No bikes in storage")
        else:
            [print(f"{object.name}: {object.price} kr") for object in list_of_bikes]
    except:
        pass


def remove_bike(list_of_bikes) -> list:
    while True:
        try:
            [print(f"{object.name}: {object.price} kr") for object in list_of_bikes]
            remove_index = int(
                input(
                    "Write the position of the bike you want to remove (The list starts at 0):\n"
                )
            )
            list_of_bikes.remove(list_of_bikes[remove_index])
            break
        except ValueError:
            print("That was not a number. Try again.")
        except IndexError:
            print("That number is not represented on the list. Try again.")
        except:
            pass
    return list_of_bikes


def show_most_expensive_bike_price(list_of_bikes) -> None:
    try:
        list_of_prices = [bike.price for bike in list_of_bikes]
        list_of_prices.reverse()
        print(f"{list_of_prices[0]} kr")
    except IndexError:
        print("No bikes in storage")
    except:
        pass


while True:
    [print(action) for action in dict_of_operations]
    action_input = input("Type one of previous actions to execute it:\n")
    while not len(difflib.get_close_matches(action_input, dict_of_operations.keys())):
        print("Input did not match any alternative")
        [print(action) for action in dict_of_operations]
        action_input = input("Type one of previous actions to execute it:\n")
    exec(
        dict_of_operations[
            difflib.get_close_matches(action_input, dict_of_operations.keys())[0]
        ]
    )
    print("")
