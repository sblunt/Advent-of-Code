from functools import lru_cache
import numpy as np
import sys

sys.setrecursionlimit(10_000)


@lru_cache(maxsize=None)
def get_price(A_rule, B_rule, X, Y):

    if X < 0 or Y < 0:
        return np.inf, np.inf, np.inf

    if X == 0 and Y == 0:
        return 0, 0, 0
    else:

        Anext_cost, Anext_A_presses, Anext_B_presses = get_price(
            A_rule, B_rule, X - A_rule[0], Y - A_rule[1]
        )
        Bnext_cost, Bnext_A_presses, Bnext_B_presses = get_price(
            A_rule, B_rule, X - B_rule[0], Y - B_rule[1]
        )

        if 3 + Anext_cost <= 1 + Bnext_cost:
            if 1 + Anext_A_presses <= 100:
                return 3 + Anext_cost, 1 + Anext_A_presses, Anext_B_presses
            else:
                return np.inf, np.inf, np.inf
        else:
            if 1 + Bnext_B_presses <= 100:
                return 1 + Bnext_cost, Bnext_A_presses, 1 + Bnext_B_presses
            else:
                return np.inf, np.inf, np.inf


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
    X_prize = int(line.split(",")[0].split("=")[1])
    Y_prize = int(line.split(",")[1].split("=")[1])

    cost, _, _ = get_price(A_rule, B_rule, X_prize, Y_prize)

    if cost != np.inf:
        print(X_prize, Y_prize, cost)
        total_cost += cost

    line = f.readline()
    line = f.readline()

print(total_cost)
