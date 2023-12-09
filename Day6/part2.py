import pandas as pd
import numpy as np

races_df = pd.read_csv(
    "input.txt", delim_whitespace=True, usecols=range(1, 5), header=None
)

time = ""
record = ""
for i in races_df.columns:
    time += str(races_df[i][0])
    record += str(races_df[i][1])

time = int(time)
record = int(record)

min_winning_time = 0.5 * (time - np.sqrt(time**2 - 4 * record))
max_winning_time = 0.5 * (time + np.sqrt(time**2 - 4 * record))

# need number of integers between the min and max winning times
first_integer_winning_time = np.floor(min_winning_time) + 1
last_integer_winning_time = np.ceil(max_winning_time) - 1

number_of_winners = last_integer_winning_time - first_integer_winning_time + 1

print("Number of winners: {}".format(int(number_of_winners)))
