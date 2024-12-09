import numpy as np


def all_sumproducts(possible_nums):

    if len(possible_nums) == 2:
        return np.array(
            [
                possible_nums[0] * possible_nums[1],
                possible_nums[0] + possible_nums[1],
                int(str(possible_nums[1]) + str(possible_nums[0])),
            ]
        )
    else:

        return np.concatenate(
            [
                possible_nums[0] * all_sumproducts(possible_nums[1:]),
                possible_nums[0] + all_sumproducts(possible_nums[1:]),
                [
                    int(str(i) + str(possible_nums[0]))
                    for i in all_sumproducts(possible_nums[1:])
                ],
            ]
        )


f = open("input.txt", "r")
test_values_sum = 0
for i, line in enumerate(f.readlines()):
    print(f"{i}", end="\r")

    target = int(line.split(":")[0])
    possibilities = np.array(line.split(":")[1].split()).astype(int)

    all_sumproducts_for_line = all_sumproducts(possibilities[::-1])
    if len(np.where(all_sumproducts_for_line == target)[0]) > 0:
        test_values_sum += target

print(test_values_sum)
f.close()
