import numpy as np
import re

"""
only check positions that are on the existing path (cuts out 70% of positions)
"""


def get_starting_move(mymap):

    directions = {"v": "down", "^": "up", "<": "left", ">": "right"}

    for i, row in enumerate(mymap):
        res = re.search("[v^><]", row)
        if res:
            curr_row = i
            curr_col = res.span()[0]
            curr_direction = directions[res.group(0)]
    return (curr_row, curr_col, curr_direction)


def solve_maze(mymap, moves_in_order, all_moves):
    row_len = len(mymap)
    col_len = len(mymap[0])

    curr_row = moves_in_order[-1][0]
    curr_col = moves_in_order[-1][1]
    curr_direction = moves_in_order[-1][2]

    while (
        curr_row < row_len - 1
        and curr_row >= 1
        and curr_col < col_len - 1
        and curr_col >= 1
    ):

        if curr_direction == "down":
            if mymap[curr_row + 1][curr_col] != "#":
                next_move = (
                    curr_row + 1,
                    curr_col,
                    curr_direction,
                )
            else:
                next_move = (curr_row, curr_col, "left")

        elif curr_direction == "up":
            if mymap[curr_row - 1][curr_col] != "#":
                next_move = (
                    curr_row - 1,
                    curr_col,
                    curr_direction,
                )
            else:
                next_move = (curr_row, curr_col, "right")

        elif curr_direction == "left":
            if mymap[curr_row][curr_col - 1] != "#":
                next_move = (
                    curr_row,
                    curr_col - 1,
                    curr_direction,
                )
            else:
                next_move = (curr_row, curr_col, "up")

        elif curr_direction == "right":
            if mymap[curr_row][curr_col + 1] != "#":
                next_move = (
                    curr_row,
                    curr_col + 1,
                    curr_direction,
                )

            else:
                next_move = (curr_row, curr_col, "down")

        if next_move in all_moves:
            raise ValueError("infinite loop detected!")
        else:
            moves_in_order.append(next_move)
            all_moves.add(next_move)

        curr_row, curr_col, curr_direction = (next_move[0], next_move[1], next_move[2])

    return moves_in_order, all_moves


if __name__ == "__main__":
    mymap = np.loadtxt("input.txt", dtype=str, comments=None)
    first_move = get_starting_move(mymap)
    mymap = np.array([list(i) for i in mymap])
    row_len = len(mymap)
    col_len = len(mymap[0])

    # solve the maze to get the locations where an obstacle
    # would change the path
    all_moves = {first_move}
    moves_in_order = [first_move]

    moves_in_order, all_previous_moves = solve_maze(mymap, moves_in_order, all_moves)

    # now add obstacles and solve the maze again
    successful_obstacles = np.zeros(
        (row_len, col_len), dtype=int
    )  # account for duplicates

    for i in range(len(moves_in_order) - 1):

        moves_in_order_subset = moves_in_order[: i + 1]
        previous_moves = {move for move in moves_in_order_subset}
        previous_positions = {(move[0], move[1]) for move in moves_in_order_subset}
        mymap_copy = np.copy(mymap)

        curr_row = moves_in_order_subset[-1][0]
        curr_col = moves_in_order_subset[-1][1]
        curr_dir = moves_in_order_subset[-1][2]

        # add an obstacle in the path
        if curr_dir == "up":
            obstacle_loc = (curr_row - 1, curr_col)
        elif curr_dir == "down":
            obstacle_loc = (curr_row + 1, curr_col)
        elif curr_dir == "left":
            obstacle_loc = (curr_row, curr_col - 1)
        elif curr_dir == "right":
            obstacle_loc = (curr_row, curr_col + 1)
        if mymap_copy[obstacle_loc] == "#" or obstacle_loc in previous_positions:
            continue
        else:
            mymap_copy[obstacle_loc] = "#"

        try:
            solve_maze(mymap_copy, moves_in_order_subset, previous_moves)
        except ValueError as e:
            successful_obstacles[obstacle_loc] = 1

    print(np.sum(successful_obstacles))
