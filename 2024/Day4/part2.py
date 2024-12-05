import numpy as np

og_input = np.loadtxt("input.txt", dtype=str)

# cast as 2d numpy array of str
og_input = np.array([list(i) for i in og_input])

rotated90 = np.rot90(og_input)
rotated180 = np.rot90(rotated90)
rotated270 = np.rot90(rotated180)


def search_ms_on_left(i, j, input_arr):
    if i < 2 or j < 2:
        return 0
    if (
        input_arr[i - 1][j - 1] == "A"
        and input_arr[i - 2][j - 2] == "M"
        and input_arr[i][j - 2] == "M"
        and input_arr[i - 2][j] == "S"
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
            if current_letter == "S":
                n_words += search_ms_on_left(i, j, inp)

print(n_words)
