import functools

f = open("input.txt", "r")

lines = f.readlines()

designs = lines[0].split("\n")[0].split(", ")
towels = []

for line in lines[2:]:
    towels.append(line.split()[0])


@functools.lru_cache
def is_possible(towel):

    if len(towel) == 0:
        return True
    for design in designs:
        if towel[: len(design)] == design:
            possible = is_possible(towel[len(design) :])
            if possible:
                return True
    return False


num_possibilities = 0
for towel in towels:
    if is_possible(towel):
        num_possibilities += 1

print(num_possibilities)
