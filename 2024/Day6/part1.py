import numpy as np
import re

mymap = np.loadtxt("input.txt", dtype=str, comments=None)

row_len = len(mymap)
col_len = len(mymap[0])

visited_positions = np.zeros((row_len, col_len), dtype=int)

directions = {"v": "down", "^": "up", "<": "left", ">": "right"}

for i, row in enumerate(mymap):
    res = re.search("[v^><]", row)
    if res:
        curr_row = i
        curr_col = res.span()[0]
        curr_direction = directions[res.group(0)]

visited_positions[curr_row, curr_col] = 1
while (
    curr_row < row_len - 1
    and curr_row >= 1
    and curr_col < col_len - 1
    and curr_col >= 1
):

    if curr_direction == "down":
        if mymap[curr_row + 1][curr_col] != "#":
            curr_row += 1

            visited_positions[curr_row, curr_col] = 1
        else:
            curr_direction = "left"

    elif curr_direction == "up":
        if mymap[curr_row - 1][curr_col] != "#":
            curr_row -= 1
            visited_positions[curr_row, curr_col] = 1
        else:
            curr_direction = "right"

    elif curr_direction == "left":
        if mymap[curr_row][curr_col - 1] != "#":
            curr_col -= 1
            visited_positions[curr_row, curr_col] = 1
        else:
            curr_direction = "up"

    elif curr_direction == "right":
        if mymap[curr_row][curr_col + 1] != "#":
            curr_col += 1
            visited_positions[curr_row, curr_col] = 1
        else:
            curr_direction = "down"
visited_positions[curr_row, curr_col] = 1

print(np.sum(visited_positions))
