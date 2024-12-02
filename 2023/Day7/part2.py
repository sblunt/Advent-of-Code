import pandas as pd
from functools import cmp_to_key

card_points = {
    "J": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "Q": 11,
    "K": 12,
    "A": 13,
}


def hand_to_dict(hand):
    num_of_each_kind = {}
    for card in hand:
        if card in num_of_each_kind.keys():
            num_of_each_kind[card] += 1
        else:
            num_of_each_kind[card] = 1
    return num_of_each_kind


def compare_equal_type_hands(hand1, hand2):
    """
    If hand1 is better, return 1.
    If hand2 is better, return -1.
    If they're equal, return 0.
    """
    for i in range(5):
        hand1_card_i_value = card_points[hand1[i]]
        hand2_card_i_value = card_points[hand2[i]]
        if hand1_card_i_value > hand2_card_i_value:
            return 1
        elif hand1_card_i_value < hand2_card_i_value:
            return -1
        else:
            continue

    return 0


def is_five_of_a_kind(hand_dict):
    # all 5 cards are the same kind
    if len(hand_dict.keys()) == 1:
        return True

    # if there are two types of cards, one must be a joker to be 5 of a kind
    elif len(hand_dict.keys()) == 2 and "J" in hand_dict.keys():
        return True

    return False


def is_four_of_a_kind(hand_dict):
    if not "J" in hand_dict.keys():
        if len(hand_dict.keys()) == 2:
            for key in hand_dict.keys():
                if hand_dict[key] not in [1, 4]:
                    return False
            return True

        return False
    else:  # at least one card is a joker
        if len(hand_dict.keys()) == 3:
            # for this situation to work, we need exactly 1 card that is neither
            # joker nor other type
            for key in hand_dict.keys():
                if hand_dict[key] == 1 and not key == "J":
                    return True
                else:
                    continue
            return False
        return False


def is_full_house(hand_dict):
    if not "J" in hand_dict.keys():
        if len(hand_dict.keys()) != 2:
            return False
        if len(hand_dict.keys()) == 2:
            for key in hand_dict.keys():
                if hand_dict[key] not in [3, 2]:
                    return False
            return True

    else:  # at least one card is a joker
        if len(hand_dict.keys()) == 3:
            return True
        return False


def is_three_of_a_kind(hand_dict):
    if not "J" in hand_dict.keys():
        if len(hand_dict.keys()) != 3:
            return False
        else:
            for key in hand_dict.keys():
                if hand_dict[key] in [3, 1]:
                    continue
                else:
                    return False
            return True
    else:
        # either we have two jokers or we have two of something else
        if hand_dict["J"] == 2:
            return True
        for key in hand_dict.keys():
            if hand_dict[key] == 2:
                return True
        return False


def is_two_pair(hand_dict):
    if "J" not in hand_dict.keys():
        if len(hand_dict.keys()) != 3:
            return False
        else:
            for key in hand_dict.keys():
                if hand_dict[key] not in [2, 1]:
                    return False
            return True
    else:
        # either we have two jokers or we have two of something else
        if hand_dict["J"] == 2:
            return True
        for key in hand_dict.keys():
            if hand_dict[key] == 2:
                return True
        return False


def is_one_pair(hand_dict):
    if len(hand_dict.keys()) == 4:
        return True
    elif "J" in hand_dict.keys():
        return True
    return False


def get_type(hand_dict):
    if is_five_of_a_kind(hand_dict):
        return 6
    if is_four_of_a_kind(hand_dict):
        return 5
    if is_full_house(hand_dict):
        return 4
    if is_three_of_a_kind(hand_dict):
        return 3
    if is_two_pair(hand_dict):
        return 2
    if is_one_pair(hand_dict):
        return 1
    return 0


def compare_hands(tuple1, tuple2):
    """

    Args:
        tuple1: tuple of 1) 5-element string representing first hand, 2) bid (int)
        tuple2: same for second hand

    Returns:
        int: 1 if hand 1 is better, -1 if hand 2 is better, 0 if they are equal
    """

    # dictionary to keep track of how many of each kind in the hand
    hand1_str = tuple1[0]
    hand2_str = tuple2[0]

    hand1_type = get_type(hand_to_dict(hand1_str))
    hand2_type = get_type(hand_to_dict(hand2_str))

    if hand1_type > hand2_type:
        return 1
    elif hand1_type < hand2_type:
        return -1
    else:
        return compare_equal_type_hands(hand1_str, hand2_str)


def sort_hands(hands_dataframe):
    # convert to needed input form for python sorting
    list_of_tuples = [(df.hand[i], df.bid[i]) for i in range(len(hands_dataframe))]

    sorted_list_of_tuples = sorted(list_of_tuples, key=cmp_to_key(compare_hands))
    return sorted_list_of_tuples


if __name__ == "__main__":
    df = pd.read_csv(
        "test_input.txt",
        delim_whitespace=True,
        names=["hand", "bid"],
    )

    # count winnings!
    sorted_hands = sort_hands(df)
    total_winnings = 0
    for i, hand_tuple in enumerate(sorted_hands):
        bid = hand_tuple[1]
        total_winnings += (i + 1) * bid
    print("Total winnings: {}".format(total_winnings))
