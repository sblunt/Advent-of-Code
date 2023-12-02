import pandas as pd

# read in inputs
df = pd.read_csv("input.txt", names=["original"])

regexp_to_match = "(\d|one|two|three|four|five|six|seven|eight|nine)"
regexp_to_match_backward = "(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)"

df["first_nums"] = df["original"].str.extract(
    regexp_to_match
)  # extract the first numeral or English number
df["last_nums"] = (
    df["original"]
    .str[::-1]  # reverse the string and extract the first numeral
    .str.extract(regexp_to_match_backward)
)
df["last_nums"] = df["last_nums"].str[::-1]


def replace_numerals(myseries):
    return (
        myseries.str.replace("nine", "9")
        .str.replace("eight", "8")
        .str.replace("seven", "7")
        .str.replace("six", "6")
        .str.replace("five", "5")
        .str.replace("four", "4")
        .str.replace("three", "3")
        .str.replace("two", "2")
        .str.replace("one", "1")
    )


df["last_nums"] = replace_numerals(df["last_nums"])
df["first_nums"] = replace_numerals(df["first_nums"])
df["nums"] = (df["first_nums"] + df["last_nums"]).astype(int)
print("Part 2 answer: {}".format(df["nums"].sum()))
