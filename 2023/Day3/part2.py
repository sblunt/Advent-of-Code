import numpy as np

schematic = np.loadtxt(
    "input.txt",
    dtype=str,
    comments=None,
)

n_cols = len(schematic[0])
n_rows = len(schematic)


def get_adjacent_nums_in_row(j, i):
    """
    Finds the values of adjacent numbers in a row of three.

    If there's a number in the middle spot, there is 1.
    If there's not a number in the middle spot, there is 1 for the first and last
    spot, if they are filled.

    Args:
        mystr (str): a three-item string

    Returns:
        list of ints: the full values of the adjacent numbers

    """
    list_of_nums = []
    if schematic[i][j].isnumeric():
        start_of_number = get_number_ending_at_idx(j, i)
        end_of_number = get_number_starting_at_idx(j, i)
        list_of_nums.append(int(start_of_number + end_of_number[1:]))
    else:
        if schematic[i][j - 1].isnumeric():
            list_of_nums.append(int(get_number_ending_at_idx(j - 1, i)))
        if schematic[i][j + 1].isnumeric():
            list_of_nums.append(int(get_number_starting_at_idx(j + 1, i)))

    return list_of_nums


def get_number_ending_at_idx(ending_idx, i):
    current_num = schematic[i][ending_idx]
    if not current_num.isnumeric():
        return ""
    if ending_idx == 0:
        if current_num.isnumeric():
            return current_num
    else:
        return get_number_ending_at_idx(ending_idx - 1, i) + current_num


def get_number_starting_at_idx(starting_idx, i):
    current_num = schematic[i][starting_idx]
    if not current_num.isnumeric():
        return ""
    if starting_idx == n_cols:
        if current_num.isnumeric():
            return current_num
    else:
        return current_num + get_number_starting_at_idx(starting_idx + 1, i)


gear_products_sum = 0

for i in range(n_rows):
    for j in range(n_cols):
        if schematic[i][j] == "*":
            # count up the number of numbers adjacent
            num_adjacent = 0
            adjacent_numbers = []
            # check to the left if we're not in the first column
            if j > 0:
                if schematic[i][j - 1].isnumeric():
                    adjacent_numbers.append(int(get_number_ending_at_idx(j - 1, i)))
                    num_adjacent += 1

            # check to the right if we're not in the last column
            if j < n_cols - 1:
                if schematic[i][j + 1].isnumeric():
                    adjacent_numbers.append(int(get_number_starting_at_idx(j + 1, i)))
                    num_adjacent += 1

            # check above if we're not in the first row
            if i > 0:
                adj_nums = get_adjacent_nums_in_row(j, i - 1)
                adjacent_numbers.extend(adj_nums)
                num_adjacent += len(adj_nums)

            # check below if we're not in the last row
            if i < n_rows - 1:
                adj_nums = get_adjacent_nums_in_row(j, i + 1)
                adjacent_numbers.extend(adj_nums)
                num_adjacent += len(adj_nums)

            if len(adjacent_numbers) == 2:
                gear_ratio = np.prod(adjacent_numbers)
                gear_products_sum += gear_ratio

print(gear_products_sum)
