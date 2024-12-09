import numpy as np

f = open("input.txt", "r")
disk_map = f.readline()
f.close()

original_block_map = []

file_id = 0
block_position = 0
for i, chr_i in enumerate(disk_map):

    # even indices = blocks
    if i % 2 == 0:
        for j in range(int(chr_i)):

            original_block_map.append(str(file_id))
            block_position += 1
        file_id += 1
    # odd indices = spaces
    elif i % 2 == 1:
        for j in range(int(chr_i)):
            original_block_map.append(".")

block_array = np.array(original_block_map)

fwd_idx = 0
back_idx = len(block_array) - 1

while fwd_idx < back_idx:
    if block_array[fwd_idx] != ".":

        fwd_idx += 1

    else:
        while block_array[back_idx] == ".":
            back_idx -= 1
        block_array[fwd_idx] = block_array[back_idx]
        block_array[back_idx] = "."

        fwd_idx += 1
        back_idx -= 1

checksum = 0
for i, num in enumerate(block_array):
    if num == ".":
        break
    checksum += i * int(num)
print(checksum)
