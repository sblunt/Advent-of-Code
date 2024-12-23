"""
so my program only ever outputs register B
and it only has one jump op, so it just repeats the whole thing over and over again
until reg A = 0

so-- one output per repeat
we must do 16 repeats

2,4-> regB = regA % 8
1,1-> regB = regB ^ 1 = (regA % 8) ^ 1
7,5-> regC = regA / 2**regB = regA/2**((regA % 8) ^ 1)
1,5-> regB = ((regA % 8) ^ 1) ^ 5
0,3-> regA = regA / 2^3 = floor(regA / 8)
4,3-> regB = regB ^ regC = (((regA % 8) ^ 1) ^ 5) ^ (regA/2**((regA % 8) ^ 1))
5,5-> output regB % 8 = ((((regA % 8) ^ 1) ^ 5) ^ (regA/2**((regA % 8) ^ 1))) % 8
3,0-> go back to beginning

so at the end of one iteration:
output = ((((regA % 8) ^ 1) ^ 5) ^ (regA // 2 ** ((regA % 8) ^ 1))) % 8
regA = regA // 8
and this continues until regA < 8

Each iteration determines the value of exactly three bits, so we just
need to figure out what those are after each iteration then add them all together.
"""

import numpy as np
from part1 import Computer

program = Computer(file="input.txt").program


possible_bits = np.arange(8)
prog_len = len(program)


def get_answer(i, answer):
    base8 = prog_len - i - 1
    working_bits = []
    for j in possible_bits:
        proposal = j * (8**base8)

        myComputer = Computer(file="input.txt")
        myComputer.registerA = answer + proposal
        myComputer.execute_program()

        while len(myComputer.output) < prog_len:
            myComputer.output.insert(0, 0)

        if myComputer.output[base8] == program[base8]:
            working_bits.append(j)

    if len(working_bits) == 0:
        return []
    elif i == prog_len - 1:
        return [answer + working_bits[0]]
    else:
        possible_answers = []
        for bit in working_bits:
            possible_answer = get_answer(i + 1, answer + (bit * (8**base8)))
            possible_answers += possible_answer

        return possible_answers


answers = get_answer(0, 0)
print(min(answers))
