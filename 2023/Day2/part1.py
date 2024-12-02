import numpy as np
import re


games = np.loadtxt("input.txt", dtype=str, delimiter=":")
game_ids = games[:, 0]
game_outcomes = games[:, 1]

max_red = 12
max_green = 13
max_blue = 14

game_id_sums = 0


def _get_num_cubes(my_group_object):
    if my_group_object is None:
        return 0
    else:
        return int(my_group_object.group(0))


for id, game in zip(game_ids, game_outcomes):
    sets = game.split(";")
    for set in sets:
        n_red = _get_num_cubes(re.search("\d+ (?=red)", set))
        n_blue = _get_num_cubes(re.search("\d+ (?=blue)", set))
        n_green = _get_num_cubes(re.search("\d+ (?=green)", set))
        if n_red > max_red or n_blue > max_blue or n_green > max_green:
            break
    else:  # if we got through every set without a break, the game was possible
        winning_game_id = int(id.split("Game ")[1])
        game_id_sums += winning_game_id

print("Sum of possible game IDs: {}".format(game_id_sums))
