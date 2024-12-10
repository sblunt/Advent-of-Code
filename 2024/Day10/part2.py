import numpy as np

topo_map = np.loadtxt(
    "input.txt",
    dtype=str,
)
num_rows = len(topo_map)
num_cols = len(topo_map[0])


def num_trails(i, j, num):
    if num == 9:

        return 1
    else:

        n_trails_total = 0

        # check left
        if j > 0:
            if int(topo_map[i][j - 1]) == num + 1:
                n_trails_total += num_trails(i, j - 1, num + 1)

        # check right
        if j < num_cols - 1:
            if int(topo_map[i][j + 1]) == num + 1:
                n_trails_total += num_trails(i, j + 1, num + 1)

        # check up
        if i > 0:
            if int(topo_map[i - 1][j]) == num + 1:
                n_trails_total += num_trails(i - 1, j, num + 1)

        # check down
        if i < num_rows - 1:
            if int(topo_map[i + 1][j]) == num + 1:
                n_trails_total += num_trails(i + 1, j, num + 1)

        return n_trails_total


trailhead_score = 0
for row in range(num_rows):
    for col in range(num_cols):
        if topo_map[row][col] == "0":
            trailhead_score += num_trails(row, col, 0)

print(trailhead_score)
