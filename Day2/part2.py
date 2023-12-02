import numpy as np
import re


games = np.loadtxt("input.txt", dtype=str, delimiter=":")
game_ids = games[:, 0]
game_outcomes = games[:, 1]

game_id_sums = 0


def _get_num_cubes(my_group_object):
    if my_group_object is None:
        return 0
    else:
        return int(my_group_object.group(0))


total_power = 0
for id, game in zip(game_ids, game_outcomes):
    sets = game.split(";")
    max_red = 0
    max_blue = 0
    max_green = 0
    for set in sets:
        n_red = _get_num_cubes(re.search("\d+ (?=red)", set))
        n_blue = _get_num_cubes(re.search("\d+ (?=blue)", set))
        n_green = _get_num_cubes(re.search("\d+ (?=green)", set))
        if n_red > max_red:
            max_red = n_red
        if n_green > max_green:
            max_green = n_green
        if n_blue > max_blue:
            max_blue = n_blue
    power = max_blue * max_green * max_red
    total_power += power

print("Sum of powers: {}".format(total_power))
