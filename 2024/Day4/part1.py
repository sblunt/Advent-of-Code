import numpy as np

og_input = np.loadtxt("input.txt", dtype=str)

# cast as 2d numpy array of str
og_input = np.array([list(i) for i in og_input])

rotated90 = np.rot90(og_input)
rotated180 = np.rot90(rotated90)
rotated270 = np.rot90(rotated180)


def search_up(i, j, input_arr):
    if i < 3:
        return 0
    if (
        input_arr[i - 1][j] == "M"
        and input_arr[i - 2][j] == "A"
        and input_arr[i - 3][j] == "S"
    ):
        return 1
    else:
        return 0


def search_diagupleft(i, j, input_arr):
    if i < 3 or j < 3:
        return 0
    if (
        input_arr[i - 1][j - 1] == "M"
        and input_arr[i - 2][j - 2] == "A"
        and input_arr[i - 3][j - 3] == "S"
    ):
        return 1
    else:
        return 0


n_words = 0

for inp in [
    og_input,
    rotated90,
    rotated180,
    rotated270,
]:
    n_rows = len(inp)
    n_cols = len(inp[0])
    for i in range(n_rows):
        for j in range(n_cols):
            current_letter = inp[i][j]
            if current_letter == "X":
                n_words += search_up(i, j, inp) + search_diagupleft(i, j, inp)

print(n_words)
