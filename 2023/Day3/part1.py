import numpy as np

schematic = np.loadtxt("input.txt", dtype=str, comments=None)

n_cols = len(schematic[0])
n_rows = len(schematic)
symbols = "*@#$%&-+=/"

part_number_sum = 0

for i in range(n_rows):
    current_number = ""
    for j in range(n_cols):
        if schematic[i][j].isnumeric():
            # fun fact: this used to be O(N^2) but apparently now it's O(N)!
            current_number += schematic[i][j]

            # check if we've reached the end of a number
            number_complete = False
            if j == n_cols - 1:
                number_complete = True
            elif not schematic[i][j + 1].isnumeric():
                number_complete = True

            if number_complete:
                if len(current_number) > 0:
                    # define the indices of the number
                    first_idx = j - len(current_number) + 1
                    last_idx = j

                    prev_idx = np.max([first_idx - 1, 0])
                    after_idx = np.min([last_idx + 1, n_cols - 1])

                    # if we're not in the first row, check the row above for symbols
                    if i > 0:
                        above = schematic[i - 1][prev_idx : after_idx + 1]
                        if len(set(above).intersection(set(symbols))) > 0:
                            part_number_sum += int(current_number)
                            current_number = ""
                            continue

                    # if we're not in the first column, check previous column for symbols
                    if first_idx > 0:
                        left = schematic[i][prev_idx]
                        if len(set(left).intersection(set(symbols))) > 0:
                            part_number_sum += int(current_number)
                            current_number = ""
                            continue

                    # if we're not in the last column, check next column for symbols
                    if last_idx < n_cols - 1:
                        right = schematic[i][after_idx]
                        if len(set(right).intersection(set(symbols))) > 0:
                            part_number_sum += int(current_number)
                            current_number = ""
                            continue

                    # if we're not in the last row, check the row below for symbols
                    if i < n_rows - 1:
                        below = schematic[i + 1][prev_idx : after_idx + 1]
                        if len(set(below).intersection(set(symbols))) > 0:
                            part_number_sum += int(current_number)
                            current_number = ""
                            continue
                    current_number = ""

print("Sum of part numbers: {}".format(part_number_sum))
