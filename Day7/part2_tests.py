from part2 import get_type, hand_to_dict

assert get_type(hand_to_dict("QQQQQ")) == 6
assert get_type(hand_to_dict("QQQQJ")) == 6
assert get_type(hand_to_dict("JJQQJ")) == 6

assert get_type(hand_to_dict("QQQQ3")) == 5
assert get_type(hand_to_dict("QQQJ3")) == 5
assert get_type(hand_to_dict("QQJJ3")) == 5
assert get_type(hand_to_dict("JJJJ3")) == 6

assert get_type(hand_to_dict("22323")) == 4
assert get_type(hand_to_dict("2232J")) == 5


print("tests passed <3")
