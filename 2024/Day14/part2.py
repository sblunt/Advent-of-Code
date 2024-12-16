import numpy as np

n_cols = 101
n_rows = 103

positions = np.zeros((n_rows, n_cols))


f = open("input.txt", "r")
input_lines = f.readlines()
num_robots = len(input_lines)

xs = np.zeros(num_robots)
ys = np.zeros(num_robots)
vys = np.zeros(num_robots)
vxs = np.zeros(num_robots)

for i, line in enumerate(input_lines):
    ys[i] = int(line.split(" ")[0].split("=")[1].split(",")[0])
    xs[i] = int(line.split(" ")[0].split("=")[1].split(",")[1])

    vys[i] = int(line.split(" ")[1].split("=")[1].split(",")[0])
    vxs[i] = int(line.split(" ")[1].split("=")[1].split(",")[1])


def display_positions(positions):

    for row in positions:
        row_display = row.astype(str)
        row_display[row_display == "0"] = "."
        print("".join(row_display))


num_seconds = 0
keep_going = True
while keep_going:
    positions = np.zeros((n_rows, n_cols), dtype=int)
    for i in range(num_robots):
        xs[i] += vxs[i]
        ys[i] += vys[i]

        xs[i] %= n_rows
        ys[i] %= n_cols

        positions[int(xs[i]), int(ys[i])] += 1

    # count up the number of diagonals in a row
    # if there are a lot of diagonals in a row, there's likely some structure
    n_diags = 0
    for i in range(n_rows):
        for j in range(n_cols):
            if positions[i][j] != 0:
                if i > 0 and j > 0:
                    # check if diag up left is same
                    if positions[i - 1][j - 1] == positions[i][j]:
                        n_diags += 1
                if i > 0 and j < n_cols - 1:
                    # check if diag up right is same
                    if positions[i - 1][j + 1] == positions[i][j]:
                        n_diags += 1

    if n_diags > 100:
        display_positions(positions)

        if (
            input('Type "stop" if you see a Christmas tree, otherwise enter: ')
            == "stop"
        ):
            keep_going = False

    num_seconds += 1

print(num_seconds)
