import numpy as np

n_cols = 101
n_rows = 103

final_positions = np.zeros((n_rows, n_cols))

n_iterations = 100


f = open("input.txt", "r")
for line in f.readlines():
    y = int(line.split(" ")[0].split("=")[1].split(",")[0])
    x = int(line.split(" ")[0].split("=")[1].split(",")[1])

    v_y = int(line.split(" ")[1].split("=")[1].split(",")[0])
    v_x = int(line.split(" ")[1].split("=")[1].split(",")[1])

    for t in range(n_iterations):
        x += v_x
        y += v_y

        x %= n_rows
        y %= n_cols
    if x != (n_rows - 1) / 2 and y != (n_cols - 1) / 2:
        final_positions[x, y] += 1

quadrant1 = np.sum(final_positions[: (n_rows - 1) // 2, : (n_cols - 1) // 2])
quadrant2 = np.sum(final_positions[: (n_rows - 1) // 2, (n_cols - 1) // 2 :])
quadrant3 = np.sum(final_positions[(n_rows - 1) // 2 :, : (n_cols - 1) // 2])
quadrant4 = np.sum(final_positions[(n_rows - 1) // 2 :, (n_cols - 1) // 2 :])

print(quadrant1 * quadrant2 * quadrant3 * quadrant4)
