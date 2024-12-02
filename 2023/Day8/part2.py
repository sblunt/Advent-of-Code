from math import lcm

# First get the instructions
with open("input.txt", "r") as f:
    instructions = f.readline()[:-1]

    # skip the blank line
    f.readline()

    network = {}
    lines_ending_in_A = []
    for line in f:
        splitline = line.split("=")
        hash = splitline[0][:-1]
        key1 = splitline[1].split(",")[0].split("(")[1]
        key2 = splitline[1].split(",")[1].split(")")[0][1:]

        network[hash] = (key1, key2)

        if hash.endswith("A"):
            lines_ending_in_A.append(hash)


# For a given start key, step through, saving the hash and instruction index for
# everything that ends in Z. If we get to the same combo, that means we've entered
# an infinite loop.
def find_the_Zs(current_key):
    instruction_idx = 0
    number_of_steps = 0
    Zs_list = []

    while "{}{}".format(current_key, instruction_idx) not in Zs_list:
        if instructions[instruction_idx] == "L":
            current_key = network[current_key][0]
        else:
            current_key = network[current_key][1]

        instruction_idx += 1
        if instruction_idx == len(instructions):
            instruction_idx = 0

        number_of_steps += 1

        if current_key.endswith("Z"):
            Zs_list.append("{}{}".format(current_key, instruction_idx))
            return number_of_steps

    return Zs_list


# (this only works because each pattern has one Z encounter per repeating loop.)
all_Z_indices = []
for i in range(len(lines_ending_in_A)):
    Z_index = find_the_Zs(lines_ending_in_A[i])
    all_Z_indices.append(Z_index)

print("Total steps: {}".format(lcm(*all_Z_indices)))
