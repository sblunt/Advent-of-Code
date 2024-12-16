import numpy as np

letter_map = np.loadtxt("input.txt", dtype=str)


n_rows = len(letter_map)
n_cols = len(letter_map[0])

assigned_indices = np.zeros((n_rows, n_cols), dtype=int)


def get_area_perimeter_prod(list_of_indices, letter_val):
    area = len(list_of_indices)
    perimeter = 0
    for i, j in list_of_indices:

        # check left
        if i == 0:
            perimeter += 1
        elif letter_map[i - 1][j] != letter_val:
            perimeter += 1

        # check right
        if i == n_rows - 1:
            perimeter += 1
        elif letter_map[i + 1][j] != letter_val:
            perimeter += 1

        # check up
        if j == 0:
            perimeter += 1
        elif letter_map[i][j - 1] != letter_val:
            perimeter += 1

        # check down
        if j == n_cols - 1:
            perimeter += 1
        elif letter_map[i][j + 1] != letter_val:
            perimeter += 1

    return area * perimeter


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


area_perimeter_product = 0
for i in range(n_rows):
    for j in range(n_cols):
        if assigned_indices[i, j] == 0:
            letter_value = letter_map[i][j]
            region_indices = [(i, j)]
            assigned_indices[i, j] = 1
            find_region_indices(i, j, letter_value)

            area_perimeter_product += get_area_perimeter_prod(
                region_indices, letter_value
            )
print(area_perimeter_product)
