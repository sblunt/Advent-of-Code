import pandas as pd
import numpy as np

input = pd.read_csv("input.txt", sep="\s+", names=["arr1", "arr2"])

input["arr1_sorted"] = np.sort(input["arr1"].values)
input["arr2_sorted"] = np.sort(input["arr2"].values)
distance = np.abs(input["arr1_sorted"].values - input["arr2_sorted"].values)
total_distance = np.sum(distance)

print(total_distance)
