import numpy as np


def get_numpresses(A_rule, B_rule, X_prize, Y_prize):
    a_x, a_y = A_rule
    b_x, b_y = B_rule

    num_presses_B = (Y_prize - X_prize * (a_y / a_x)) / (b_y - b_x * a_y / a_x)
    num_presses_A = (X_prize - num_presses_B * b_x) / a_x

    if (
        round(num_presses_A) * round(a_y) + round(num_presses_B) * round(b_y) == Y_prize
        and round(num_presses_A) * round(a_x) + round(num_presses_B) * round(b_x)
        == X_prize
    ):
        return round(num_presses_A), round(num_presses_B)
    else:
        return 0, 0


f = open("input.txt", "r")

total_cost = 0
line = f.readline()

while line:

    A_rule_X = int(line.split(",")[0].split("+")[1])
    A_rule_Y = int(line.split(",")[1].split("+")[1])
    A_rule = (A_rule_X, A_rule_Y)

    line = f.readline()
    B_rule_X = int(line.split(",")[0].split("+")[1])
    B_rule_Y = int(line.split(",")[1].split("+")[1])
    B_rule = (B_rule_X, B_rule_Y)

    line = f.readline()
    X_prize = int(line.split(",")[0].split("=")[1]) + 10000000000000
    Y_prize = int(line.split(",")[1].split("=")[1]) + 10000000000000

    numpresses_A, numpresses_B = get_numpresses(A_rule, B_rule, X_prize, Y_prize)

    if (
        numpresses_A < np.inf
        and numpresses_B < np.inf
        and numpresses_A > 0
        and numpresses_B > 0
    ):
        cost = 3 * numpresses_A + numpresses_B
        total_cost += cost

    line = f.readline()
    line = f.readline()

print(total_cost)
