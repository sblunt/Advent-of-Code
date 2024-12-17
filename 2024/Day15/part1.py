import numpy as np

f = open("input.txt", "r")

warehouse_map = []
moves = []

line = f.readline()
i = 0
while line != "\n":
    line_rep = []
    for j, line_val in enumerate(line):
        if line_val != "\n":  # (don't append newline char at end)
            line_rep.append(line_val)
        if line_val == "@":
            robot_position = [i, j]
    warehouse_map.append(line_rep)
    i += 1
    line = f.readline()

warehouse_map = np.array(warehouse_map)

n_cols = len(warehouse_map[0])
n_rows = len(warehouse_map)

line = f.readline()
while line:
    for i in line:
        if i != "\n":
            moves.append(i)
    line = f.readline()


def do_up_move(warehouse_map, robot_position):
    i = robot_position[0] - 1

    # if the next space is a ".", just move the robot up
    if warehouse_map[i, robot_position[1]] == ".":
        robot_position[0] = i
        warehouse_map[i, robot_position[1]] = "@"
        warehouse_map[i + 1, robot_position[1]] = "."
        return warehouse_map, robot_position

    # if the next space is a "#", don't move anything
    if warehouse_map[i, robot_position[1]] == "#":
        return warehouse_map, robot_position

    # if we've made it here, next space is O.
    # count number of Os between position and next # or .
    num_Os = 0
    while warehouse_map[i, robot_position[1]] != ".":
        if warehouse_map[i, robot_position[1]] == "O":
            num_Os += 1
            i -= 1
        elif warehouse_map[i, robot_position[1]] == "#":
            return warehouse_map, robot_position

    # shift all the Os up by one
    warehouse_map[
        robot_position[0] - 1 - num_Os : robot_position[0] - 1, robot_position[1]
    ] = "O"
    warehouse_map[robot_position[0] - 1, robot_position[1]] = "@"
    warehouse_map[robot_position[0], robot_position[1]] = "."
    robot_position[0] -= 1

    return warehouse_map, robot_position


for move_i in moves:

    if move_i == "^":

        warehouse_map, robot_position = do_up_move(warehouse_map, robot_position)

    elif move_i == "v":

        robot_position = [
            n_rows - robot_position[0] - 1,
            n_cols - robot_position[1] - 1,
        ]

        warehouse_map, robot_position = do_up_move(
            np.rot90(np.rot90(warehouse_map)), robot_position
        )

        warehouse_map = np.rot90(np.rot90(warehouse_map))
        robot_position = [
            n_rows - robot_position[0] - 1,
            n_cols - robot_position[1] - 1,
        ]

    elif move_i == "<":

        robot_position = [
            robot_position[1],
            n_rows - robot_position[0] - 1,
        ]

        warehouse_map, robot_position = do_up_move(
            np.rot90(np.rot90(np.rot90(warehouse_map))), robot_position
        )

        warehouse_map = np.rot90(warehouse_map)

        robot_position = [
            n_rows - 1 - robot_position[1],
            robot_position[0],
        ]

    elif move_i == ">":

        robot_position = [
            n_cols - robot_position[1] - 1,
            robot_position[0],
        ]

        warehouse_map, robot_position = do_up_move(
            np.rot90(warehouse_map), robot_position
        )

        warehouse_map = np.rot90(np.rot90(np.rot90(warehouse_map)))

        robot_position = [
            robot_position[1],
            n_cols - robot_position[0] - 1,
        ]

# calculate GPS sum
gps_sum = 0
for i in range(n_rows):
    for j in range(n_cols):
        if warehouse_map[i, j] == "O":
            gps_sum += 100 * i + j

print(gps_sum)
