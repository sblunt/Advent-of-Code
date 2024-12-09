import numpy as np

# this is very slow but I was ready to rip my hair out writing the fast version lol

f = open("input.txt", "r")
disk_map = f.readline()
f.close()

original_map = []
num_repeats = []
starting_indices = []

block_position = 0
for i, chr_i in enumerate(disk_map):

    # even indices = blocks
    if i % 2 == 0:

        for j in range(int(chr_i)):
            original_map.append(i // 2)

        starting_indices.append(block_position)
        num_repeats.append(int(chr_i))
        block_position += int(chr_i)

    # odd indices = spaces
    elif i % 2 == 1:

        block_position += int(chr_i)
        for j in range(int(chr_i)):
            original_map.append(".")

original_map = np.array(original_map)


def move_number_group(whole_list, number_value, number_start_index, number_numrepeat):

    num_spaces = 0
    for i, entry in enumerate(whole_list):
        if entry == ".":
            num_spaces += 1
        else:
            num_spaces = 0

        if i < number_start_index:
            if num_spaces == number_numrepeat:

                # update new position
                whole_list[i + 1 - number_numrepeat : i + 1] = number_value

                # update old position
                whole_list[
                    number_start_index : number_start_index + number_numrepeat
                ] = "."

                return whole_list

    return whole_list


for i in reversed(range(len(num_repeats))):
    original_map = move_number_group(
        original_map, i, starting_indices[i], num_repeats[i]
    )
    print(i, end="\r")


checksum = 0
# compute checksum
for i, map_val in enumerate(original_map):
    if map_val == ".":
        map_val = 0
    checksum += int(map_val) * i
print(checksum)
