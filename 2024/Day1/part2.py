import pandas as pd

input = pd.read_csv("input.txt", sep="\s+", names=["arr1", "arr2"])

arr1 = input["arr1"].values
arr2 = input["arr2"].values

arr2_occurrence = {}
for i in arr2:
    try:
        arr2_occurrence[i] += 1
    except KeyError:
        arr2_occurrence[i] = 1

similarity = 0
for i in arr1:
    try:
        similarity += i * arr2_occurrence[i]
    except KeyError:
        pass
print(similarity)
