import pandas as pd
import numpy as np

races_df = pd.read_csv(
    "input.txt", delim_whitespace=True, usecols=range(1, 5), header=None
)

product_of_winners = 1
for i in races_df.columns:
    time = races_df[i][0]
    record = races_df[i][1]

    min_winning_time = 0.5 * (time - np.sqrt(time**2 - 4 * record))
    max_winning_time = 0.5 * (time + np.sqrt(time**2 - 4 * record))

    # need number of integers between the min and max winning times
    first_integer_winning_time = np.floor(min_winning_time) + 1
    last_integer_winning_time = np.ceil(max_winning_time) - 1

    number_of_winners = last_integer_winning_time - first_integer_winning_time + 1
    product_of_winners *= number_of_winners

print("Product of winners: {}".format(int(product_of_winners)))
