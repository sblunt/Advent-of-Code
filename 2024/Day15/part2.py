import numpy as np
import time

# this code could be significantly simplified but it works and it's cute and I don't want to work on it more lmao

f = open("input.txt", "r")

warehouse_map = []
moves = []

line = f.readline()
i = 0
while line != "\n":
    line_rep = []
    for j, line_val in enumerate(line):
        if line_val != "\n":  # (don't append newline char at end)
            if line_val == "#":
                line_rep.append("#")
                line_rep.append("#")
            elif line_val == "O":
                line_rep.append("[")
                line_rep.append("]")
            elif line_val == ".":
                line_rep.append(".")
                line_rep.append(".")
            elif line_val == "@":
                line_rep.append("@")
                line_rep.append(".")
                robot_position = [i, 2 * j]
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


# get coordinates of all adjacent boxes above. if run into #, assert that we can't make a move
def get_adjacent_box_starting_coords(i, j, warehouse_map):
    """
    Return a list of (i,j) of the [ in each box
    """

    if warehouse_map[i, j] == ".":
        return []

    elif warehouse_map[i, j] == "#":
        raise AssertionError("no move needed")

    elif warehouse_map[i, j] == "[":
        adjacent_boxes = [(i, j)]
        adjacent_boxes += get_adjacent_box_starting_coords(i - 1, j, warehouse_map)
        adjacent_boxes += get_adjacent_box_starting_coords(i - 1, j + 1, warehouse_map)
        return adjacent_boxes

    elif warehouse_map[i, j] == "]":
        adjacent_boxes = [(i, j - 1)]

        adjacent_boxes += get_adjacent_box_starting_coords(i - 1, j, warehouse_map)
        adjacent_boxes += get_adjacent_box_starting_coords(i - 1, j - 1, warehouse_map)
        return adjacent_boxes


def do_up_move(warehouse_map, robot_position):

    i = robot_position[0] - 1
    j = robot_position[1]

    # if the next space is a ".", just move the robot up
    if warehouse_map[i, j] == ".":
        robot_position[0] = i
        warehouse_map[i, j] = "@"
        warehouse_map[i + 1, j] = "."
        return warehouse_map, robot_position

    # if the next space is a "#", don't move anything
    if warehouse_map[i, j] == "#":
        return warehouse_map, robot_position

    # if we've made it here, the space immediately above is [ or ]
    try:
        adjacent_boxes = get_adjacent_box_starting_coords(i, j, warehouse_map)

        # need to sort to make sure we move topmost boxes up first
        adjacent_boxes.sort()

        # move all adjacent boxes up by 1
        for (
            i,
            j,
        ) in adjacent_boxes:
            warehouse_map[i - 1, j : j + 2] = ["[", "]"]
            warehouse_map[i, j : j + 2] = [".", "."]

        # update position of robot
        warehouse_map[robot_position[0], robot_position[1]] = "."
        warehouse_map[robot_position[0] - 1, robot_position[1]] = "@"
        robot_position[0] -= 1

    except AssertionError:
        # no moves possible
        return warehouse_map, robot_position

    return warehouse_map, robot_position


def do_left_move(warehouse_map, robot_position):
    """
    same logic as part 1
    """

    i = robot_position[0]
    j = robot_position[1] - 1

    # if the next space is a ".", just move the robot left
    if warehouse_map[i, j] == ".":
        robot_position[1] = j
        warehouse_map[i, j] = "@"
        warehouse_map[i, j + 1] = "."
        return warehouse_map, robot_position

    # if the next space is a "#", don't move anything
    if warehouse_map[i, j] == "#":
        return warehouse_map, robot_position

    # if we've made it here, next space is ].
    # count number of []s between position and next # or .
    num_boxes = 0
    while warehouse_map[i, j] != ".":
        if warehouse_map[i, j] == "]":
            num_boxes += 1
            j -= 2
        elif warehouse_map[i, j] == "#":
            return warehouse_map, robot_position

    # shift all the []s left by one
    warehouse_map[i, j : j + 2 * num_boxes] = warehouse_map[
        i, j + 1 : j + 2 * num_boxes + 1
    ]

    warehouse_map[robot_position[0], robot_position[1] - 1] = "@"
    warehouse_map[robot_position[0], robot_position[1]] = "."
    robot_position[1] -= 1

    return warehouse_map, robot_position


def do_right_move(warehouse_map, robot_position):
    """
    same logic as part 1
    """

    i = robot_position[0]
    j = robot_position[1] + 1

    # if the next space is a ".", just move the robot right
    if warehouse_map[i, j] == ".":
        robot_position[1] = j
        warehouse_map[i, j] = "@"
        warehouse_map[i, j - 1] = "."
        return warehouse_map, robot_position

    # if the next space is a "#", don't move anything
    if warehouse_map[i, j] == "#":
        return warehouse_map, robot_position

    # if we've made it here, next space is ].
    # count number of []s between position and next # or .
    num_boxes = 0
    while warehouse_map[i, j] != ".":
        if warehouse_map[i, j] == "[":
            num_boxes += 1
            j += 2
        elif warehouse_map[i, j] == "#":
            return warehouse_map, robot_position

    # shift all the []s right by one
    warehouse_map[i, robot_position[1] + 2 : robot_position[1] + 2 + 2 * num_boxes] = (
        warehouse_map[i, robot_position[1] + 1 : robot_position[1] + 1 + 2 * num_boxes]
    )

    warehouse_map[robot_position[0], robot_position[1] + 1] = "@"
    warehouse_map[robot_position[0], robot_position[1]] = "."
    robot_position[1] += 1

    return warehouse_map, robot_position


def print_map(warehouse_map):
    for i in warehouse_map:
        print("".join(list(i)))


print_map(warehouse_map)
for move_i_idx, move_i in enumerate(moves):

    if move_i == "^":

        warehouse_map, robot_position = do_up_move(warehouse_map, robot_position)

    elif move_i == "v":

        robot_position = [
            n_rows - robot_position[0] - 1,
            n_cols - robot_position[1] - 1,
        ]

        leftbrak = warehouse_map == "["
        rightbrak = warehouse_map == "]"
        warehouse_map[leftbrak] = "]"
        warehouse_map[rightbrak] = "["

        warehouse_map, robot_position = do_up_move(
            np.rot90(np.rot90(warehouse_map)), robot_position
        )

        warehouse_map = np.rot90(np.rot90(warehouse_map))

        leftbrak = warehouse_map == "["
        rightbrak = warehouse_map == "]"
        warehouse_map[leftbrak] = "]"
        warehouse_map[rightbrak] = "["

        robot_position = [
            n_rows - robot_position[0] - 1,
            n_cols - robot_position[1] - 1,
        ]

    if move_i == "<":

        warehouse_map, robot_position = do_left_move(warehouse_map, robot_position)

    elif move_i == ">":

        warehouse_map, robot_position = do_right_move(warehouse_map, robot_position)

    # why not have a little fun??
    print_map(warehouse_map)
    print("{:.2f}% done".format(100 * move_i_idx / len(moves)))
    time.sleep(0.01)

print_map(warehouse_map)

# calculate GPS sum
gps_sum = 0
for i in range(n_rows):
    for j in range(n_cols):
        if warehouse_map[i, j] == "[":

            box_coord = j + 100 * i

            gps_sum += box_coord

print(gps_sum)
