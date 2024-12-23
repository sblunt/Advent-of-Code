import functools

f = open("input.txt", "r")

lines = f.readlines()

designs = lines[0].split("\n")[0].split(", ")
towels = []

for line in lines[2:]:
    towels.append(line.split()[0])


@functools.lru_cache
def find_num_possibilities(towel):

    num_possibilities = 0
    if len(towel) == 0:
        return 1
    for design in designs:
        if towel[: len(design)] == design:
            num_possibilities += find_num_possibilities(towel[len(design) :])
    return num_possibilities


total_possibilities = 0
for towel in towels:
    total_possibilities += find_num_possibilities(towel)

print(total_possibilities)
