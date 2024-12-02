# Friendship ended with array. Now hash map is my best friend.


# First get the instructions
def build_network(filename="input.txt"):
    with open(filename, "r") as f:
        instructions = f.readline()[:-1]

        # skip the blank line
        f.readline()

        network = {}
        for line in f:
            splitline = line.split("=")
            hash = splitline[0][:-1]
            key1 = splitline[1].split(",")[0].split("(")[1]
            key2 = splitline[1].split(",")[1].split(")")[0][1:]

            network[hash] = (key1, key2)
    return instructions, network


if __name__ == "__main__":
    instructions, network = build_network()

    current_key = "AAA"
    instruction_idx = 0
    number_of_steps = 0
    while current_key != "ZZZ":
        if instructions[instruction_idx] == "L":
            current_key = network[current_key][0]
        else:
            current_key = network[current_key][1]

        instruction_idx += 1
        if instruction_idx == len(instructions):
            instruction_idx = 0

        number_of_steps += 1

    print("Number of steps: {}".format(number_of_steps))
