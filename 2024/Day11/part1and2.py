import numpy as np
import time

start = time.time()

n_blinks = 75

input_array = np.loadtxt("input.txt", dtype=str)

# dictionary of dictionaries
number_length_after_n_blinks = {}


def add_to_dict(value, n_blinks, number_length):
    if value not in number_length_after_n_blinks:
        number_length_after_n_blinks[value] = {n_blinks: number_length}
    else:
        number_length_after_n_blinks[value][n_blinks] = number_length


def compute_number_length_after_n_blinks(value, n_blinks):

    if value in number_length_after_n_blinks:
        if n_blinks in number_length_after_n_blinks[value]:
            return number_length_after_n_blinks[value][n_blinks]

    if n_blinks == 0:
        number_len = 1
        return number_len

    num_digits = len(value)

    if value == "0":
        number_len = compute_number_length_after_n_blinks("1", n_blinks - 1)

    elif num_digits % 2 == 0:
        number_len = compute_number_length_after_n_blinks(
            str(int(value[: num_digits // 2])), n_blinks - 1
        ) + compute_number_length_after_n_blinks(
            str(int(value[num_digits // 2 :])), n_blinks - 1
        )

    else:
        number_len = compute_number_length_after_n_blinks(
            str(int(value) * 2024), n_blinks - 1
        )

    add_to_dict(value, n_blinks, number_len)
    return number_len


total_array_len = 0
for val in input_array:
    total_array_len += compute_number_length_after_n_blinks(val, n_blinks)

print("time: {:.2f} s".format(time.time() - start))
print(total_array_len)
