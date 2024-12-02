import pandas as pd
import numpy as np

# read in inputs
df = pd.read_csv("input.txt", names=["original"])

first_nums = df["original"].str.extract("(\d)")  # extract the first numeral
last_nums = (
    df["original"]
    .str[::-1]  # reverse the string and extract the first numeral
    .str.extract("(\d)")
)

numbers = (first_nums + last_nums).astype(int)
sum = np.sum(numbers, axis=0).values[0]

print("Part 1 answer: {}".format(sum))
