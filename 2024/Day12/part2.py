import numpy as np

letter_map = np.loadtxt("input.txt", dtype=str)


n_rows = len(letter_map)
n_cols = len(letter_map[0])

assigned_indices = np.zeros((n_rows, n_cols), dtype=int)


def get_area_nsides_prod(list_of_indices, letter_val):
    area = len(list_of_indices)
    n_corners = 0

    # TODO: I'm dealing with outside corners but not inside corners

    # check if the index is a corner (n_sides = n_corners - 1)
    for i, j in list_of_indices:

        is_left_same = True
        if j == 0:
            is_left_same = False
        elif letter_map[i][j - 1] != letter_val:
            is_left_same = False

        is_right_same = True
        if j == n_cols - 1:
            is_right_same = False
        elif letter_map[i][j + 1] != letter_val:
            is_right_same = False

        is_up_same = True
        if i == 0:
            is_up_same = False
        elif letter_map[i - 1][j] != letter_val:
            is_up_same = False

        is_down_same = True
        if i == n_rows - 1:
            is_down_same = False
        elif letter_map[i + 1][j] != letter_val:
            is_down_same = False

        is_upleftdiag_same = True
        if i == 0 or j == 0:
            is_upleftdiag_same = False
        elif letter_map[i - 1][j - 1] != letter_val:
            is_upleftdiag_same = False

        is_uprightdiag_same = True
        if i == 0 or j == n_cols - 1:
            is_uprightdiag_same = False
        elif letter_map[i - 1][j + 1] != letter_val:
            is_uprightdiag_same = False

        is_downrightdiag_same = True
        if i == n_rows - 1 or j == n_cols - 1:
            is_downrightdiag_same = False
        elif letter_map[i + 1][j + 1] != letter_val:
            is_downrightdiag_same = False

        is_downleftdiag_same = True
        if i == n_rows - 1 or j == 0:
            is_downleftdiag_same = False
        elif letter_map[i + 1][j - 1] != letter_val:
            is_downleftdiag_same = False

        # option 1: left/up same, right/down different = +1 corner
        if is_up_same and is_left_same and not is_right_same and not is_down_same:
            n_corners += 1
        # option 2: right/up same, left/down different = +1 corner
        if is_up_same and is_right_same and not is_left_same and not is_down_same:
            n_corners += 1
        # option 3: left/down same, right/up different = +1 corner
        if is_left_same and is_down_same and not is_right_same and not is_up_same:
            n_corners += 1
        # option 4: right/down same, left/up different = +1 corner
        if is_right_same and is_down_same and not is_left_same and not is_up_same:
            n_corners += 1
        # option 5: only 1/4 adjacent is same = +2 corner
        if is_down_same + is_up_same + is_left_same + is_right_same == 1:
            n_corners += 2
        # option 6: none are same = +4 corner
        if is_down_same + is_up_same + is_left_same + is_right_same == 0:
            n_corners += 4

        # option 7: up same, right same, uprightdiag not same = +1 corner
        if is_up_same and is_right_same and not is_uprightdiag_same:
            n_corners += 1

        # option 8: up same, left same, upleftdiag not same
        if is_up_same and is_left_same and not is_upleftdiag_same:
            n_corners += 1

        # option 9: down same, right same, downrightdiag not same
        if is_down_same and is_right_same and not is_downrightdiag_same:
            n_corners += 1

        # option 10: down same, left same, downleftdiag not same
        if is_down_same and is_left_same and not is_downleftdiag_same:
            n_corners += 1

    n_sides = n_corners

    return area * n_sides


def find_region_indices(i, j, val):

    # check left
    if i - 1 >= 0:
        if letter_map[i - 1][j] == val and assigned_indices[i - 1, j] == 0:
            region_indices.append((i - 1, j))
            assigned_indices[i - 1, j] = 1
            find_region_indices(i - 1, j, val)

    # check right
    if i + 1 < n_rows:
        if letter_map[i + 1][j] == val and assigned_indices[i + 1, j] == 0:
            region_indices.append((i + 1, j))
            assigned_indices[i + 1, j] = 1
            find_region_indices(i + 1, j, val)

    # check up
    if j - 1 >= 0:
        if letter_map[i][j - 1] == val and assigned_indices[i, j - 1] == 0:
            region_indices.append((i, j - 1))
            assigned_indices[i, j - 1] = 1
            find_region_indices(i, j - 1, val)

    # check down
    if j + 1 < n_cols:
        if letter_map[i][j + 1] == val and assigned_indices[i, j + 1] == 0:
            region_indices.append((i, j + 1))
            assigned_indices[i, j + 1] = 1
            find_region_indices(i, j + 1, val)


area_nsides_product = 0
for i in range(n_rows):
    for j in range(n_cols):
        if assigned_indices[i, j] == 0:
            letter_value = letter_map[i][j]
            region_indices = [(i, j)]
            assigned_indices[i, j] = 1
            find_region_indices(i, j, letter_value)

            area_nsides_product += get_area_nsides_prod(region_indices, letter_value)
print(area_nsides_product)
