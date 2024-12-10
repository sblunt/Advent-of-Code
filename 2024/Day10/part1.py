import numpy as np

topo_map = np.loadtxt(
    "input.txt",
    dtype=str,
)
num_rows = len(topo_map)
num_cols = len(topo_map[0])


def get_trail_ends(i, j, num):
    if num == 9:

        return {(i, j)}
    else:

        left_ends = set()
        right_ends = set()
        up_ends = set()
        down_ends = set()

        # check left
        if j > 0:
            if int(topo_map[i][j - 1]) == num + 1:
                left_ends = get_trail_ends(i, j - 1, num + 1)

        # check right
        if j < num_cols - 1:
            if int(topo_map[i][j + 1]) == num + 1:
                right_ends = get_trail_ends(i, j + 1, num + 1)

        # check up
        if i > 0:
            if int(topo_map[i - 1][j]) == num + 1:
                up_ends = get_trail_ends(i - 1, j, num + 1)

        # check down
        if i < num_rows - 1:
            if int(topo_map[i + 1][j]) == num + 1:
                down_ends = get_trail_ends(i + 1, j, num + 1)

        return left_ends | down_ends | up_ends | right_ends


trailhead_score = 0
for row in range(num_rows):
    for col in range(num_cols):
        if topo_map[row][col] == "0":
            trail_ends = get_trail_ends(row, col, 0)
            trailhead_score += len(trail_ends)

print(trailhead_score)
