"""
Searching through both lists is O(M*N), but sorting both is O(MlogM + NlogN),
then searching through once is O(N+M), so sorting first gives better time complexity.

...but this is Python, so I'll expend a lot of time complexity to read in the
file anyway. :) lol.
"""

import numpy as np

# read in the input
input = np.loadtxt("input.txt", delimiter=":", dtype=str)

total_points = 0
for card in input:
    num_matches = 0

    # read in arrays of winning numbers and numbers I have
    numbers = card[1].split("| ")
    winning_numbers = np.array(numbers[0].split()).astype(int)
    my_numbers = np.array(numbers[1].split()).astype(int)

    # sort both arrays
    sorted_winning_numbers = np.sort(winning_numbers)
    sorted_my_numbers = np.sort(my_numbers)

    # iterate through winning numbers and look for matches
    my_nums_idx = 0
    winning_idx = 0
    while winning_idx < len(winning_numbers) and my_nums_idx < len(my_numbers):
        if sorted_winning_numbers[winning_idx] < sorted_my_numbers[my_nums_idx]:
            winning_idx += 1
        elif sorted_winning_numbers[winning_idx] == sorted_my_numbers[my_nums_idx]:
            num_matches += 1
            my_nums_idx += 1
            winning_idx += 1
        else:
            my_nums_idx += 1

    if num_matches > 0:
        total_points += 2 ** (num_matches - 1)

print(total_points)
