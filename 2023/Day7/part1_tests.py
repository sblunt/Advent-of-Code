import pandas as pd
from part1 import (
    hand_to_dict,
    is_five_of_a_kind,
    is_four_of_a_kind,
    is_full_house,
    is_three_of_a_kind,
    is_two_pair,
    is_one_pair,
    compare_hands,
    compare_equal_type_hands,
    get_type,
)

# five of a kind
assert is_five_of_a_kind(hand_to_dict("AAAAA"))
assert not is_five_of_a_kind(hand_to_dict("ATAAA"))

# four of a kind
assert is_four_of_a_kind(hand_to_dict("AAAAT"))
assert is_four_of_a_kind(hand_to_dict("TAAAA"))
assert is_four_of_a_kind(hand_to_dict("AATAA"))
assert not is_four_of_a_kind(hand_to_dict("AAAAA"))
assert not is_four_of_a_kind(hand_to_dict("AT5AA"))

# full house
assert is_full_house(hand_to_dict("ATAAT"))
assert is_full_house(hand_to_dict("TAATA"))
assert is_full_house(hand_to_dict("AAATT"))
assert not is_full_house(hand_to_dict("AAAAA"))
assert not is_full_house(hand_to_dict("AT5AA"))
assert not is_full_house(hand_to_dict("ATAAA"))

# three of a kind
assert is_three_of_a_kind(hand_to_dict("ATAA2"))
assert is_three_of_a_kind(hand_to_dict("TAA7A"))
assert is_three_of_a_kind(hand_to_dict("33324"))
assert not is_three_of_a_kind(hand_to_dict("AAAAA"))
assert not is_three_of_a_kind(hand_to_dict("ATTAA"))

# two pair
assert is_two_pair(hand_to_dict("AJ4JA"))
assert not is_two_pair(hand_to_dict("AJ4JJ"))
assert is_two_pair(hand_to_dict("52425"))

# one pair
assert is_one_pair(hand_to_dict("AA234"))
assert not is_one_pair(hand_to_dict("AAJJ4"))
assert not is_one_pair(hand_to_dict("AAJJJ"))

# check the comparison of equal-type hands
assert compare_equal_type_hands("AAAAA", "KKKKK") == 1
assert compare_equal_type_hands("22222", "22222") == 0
assert compare_equal_type_hands("43333", "33333") == 1
assert compare_equal_type_hands("33332", "33334") == -1

# check some of the test inputs
df = pd.read_csv(
    "test_input.txt",
    delim_whitespace=True,
    names=["hand", "bid"],
    dtype={"hand": str, "bid": int},
)

# check the type of first hand
assert get_type(hand_to_dict(df.hand[0])) == 1
assert get_type(hand_to_dict(df.hand[1])) == 3
assert get_type(hand_to_dict(df.hand[2])) == 2
assert get_type(hand_to_dict(df.hand[3])) == 2
assert get_type(hand_to_dict(df.hand[4])) == 3

# first hand should always lose
assert compare_hands((df.hand[0], 1), (df.hand[1], 1)) == -1
assert compare_hands((df.hand[0], 1), (df.hand[2], 1)) == -1
assert compare_hands((df.hand[0], 1), (df.hand[3], 1)) == -1
assert compare_hands((df.hand[0], 1), (df.hand[4], 1)) == -1

# second hand beats everything except last hand
assert compare_hands((df.hand[1], 1), (df.hand[4], 4)) == -1
assert compare_hands((df.hand[1], 1), (df.hand[0], 1)) == 1
assert compare_hands((df.hand[1], 1), (df.hand[2], 2)) == 1
assert compare_hands((df.hand[1], 1), (df.hand[3], 3)) == 1

# third hand should only lose to second and last hand
assert compare_hands((df.hand[2], 1), (df.hand[0], 4)) == 1
assert compare_hands((df.hand[2], 1), (df.hand[1], 1)) == -1
assert compare_hands((df.hand[2], 1), (df.hand[3], 2)) == 1
assert compare_hands((df.hand[2], 1), (df.hand[4], 3)) == -1

print("Tests passed <3")
