import numpy as np

f = open("input.txt", "r")

antenna_coords = {}
for i, line in enumerate(f.readlines()):
    for j, ltr in enumerate(line):
        if ltr != "." and ltr != "\n":
            try:
                antenna_coords[ltr].append((i, j))
            except KeyError:
                antenna_coords[ltr] = [(i, j)]
f.close()


def get_all_node_combos(list_of_coords):

    if len(list_of_coords) == 2:
        return [(list_of_coords[0], list_of_coords[1])]
    else:
        combos_including_first = [(list_of_coords[0], i) for i in list_of_coords[1:]]

        return combos_including_first + get_all_node_combos(list_of_coords[1:])


antinode_locations = np.zeros((i + 1, j + 1), dtype=int)
for ltr in antenna_coords.keys():
    node_locations = antenna_coords[ltr]

    matching_node_combos = get_all_node_combos(node_locations)

    for combo in matching_node_combos:

        row1, col1 = combo[0]
        row2, col2 = combo[1]

        rowdiff = row2 - row1
        antinode_row1 = row1 - rowdiff
        antinode_row2 = row2 + rowdiff

        coldiff = col2 - col1
        antinode_col1 = col1 - coldiff
        antinode_col2 = col2 + coldiff

        try:
            if antinode_row1 >= 0 and antinode_col1 >= 0:
                antinode_locations[antinode_row1, antinode_col1] = 1
        except IndexError:
            pass
        try:
            if antinode_row2 >= 0 and antinode_col2 >= 0:
                antinode_locations[antinode_row2, antinode_col2] = 1
        except IndexError:
            pass

print(np.sum(antinode_locations))
