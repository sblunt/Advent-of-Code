import numpy as np


def check_safe(level):

    level_diff = np.diff(level)

    # check that all diffs are either 1 or 2
    in_range = np.all((np.abs(level_diff) > 0) & (np.abs(level_diff) < 4))

    if in_range:
        # check that all diffs are positive or all diffs are negative
        if np.all(level_diff < 0) or np.all(level_diff > 0):
            return True

    return False


f = open("input.txt", "r")
num_safe = 0
for level in f:
    level = np.array([int(i) for i in level.split()])

    is_level_safe = check_safe(level)
    if is_level_safe:
        num_safe += 1

    if not is_level_safe:

        for i in range(len(level)):

            is_level_safe = check_safe(np.delete(level, i))
            if is_level_safe:
                num_safe += 1
                break

print(num_safe)
