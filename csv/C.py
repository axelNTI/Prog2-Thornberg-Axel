import csv


def none_filter(x):
    return x != None


with open("csv/uppgift_c.csv", "r") as file:
    reader = csv.DictReader(file, delimiter=";")
    possible_games = []
    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    for game in reader:
        game = list(filter(none_filter, list(game.values())))
        game_id = game[0].split(":")[0]
        game[0] = game[0].split(":")[1:][0]
        for i, j in enumerate(game):
            game[i] = j.split(",")
        for turn in game:
            for cubes in turn.split(" ")[1:]:
                if cubes[0] > max_cubes[cubes[1]]:
                    break
        possible_games.append(game_id)

    print(possible_games)
