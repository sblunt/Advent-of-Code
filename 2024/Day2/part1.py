import numpy as np

f = open("input.txt", "r")
num_safe = 0
for level in f:
    level = np.array([int(i) for i in level.split()])
    level_diff = np.diff(level)

    # check that all diffs are either 1 or 2
    in_range = np.all((np.abs(level_diff) > 0) & (np.abs(level_diff) < 4))

    if in_range:

        # check that all diffs are positive or all diffs are negative
        if np.all(level_diff < 0) or np.all(level_diff > 0):
            num_safe += 1

print(num_safe)
