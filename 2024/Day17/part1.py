import numpy as np


class Computer(object):
    def __init__(self, file="test_input.txt"):

        self.instruction_pointer = 0

        f = open(file, "r")

        lines = f.readlines()
        self.registerA = int(lines[0].split(": ")[1])
        self.registerB = int(lines[1].split(": ")[1])
        self.registerC = int(lines[2].split(": ")[1])

        self.program = np.array(lines[4].split(": ")[1].split(",")).astype(int)
        self.opcode = self.program[0]
        self.literal_operand = self.program[1]
        self.set_combo_operand()
        self.output = []

    def set_combo_operand(self):
        if self.literal_operand >= 0 and self.literal_operand <= 3:
            self.combo_operand = self.literal_operand
        elif self.literal_operand == 4:
            self.combo_operand = self.registerA
        elif self.literal_operand == 5:
            self.combo_operand = self.registerB
        elif self.literal_operand == 6:
            self.combo_operand = self.registerC

    def adv(self):
        self.registerA = self.registerA // (2 ** (self.combo_operand))
        self.instruction_pointer += 2

    def bxl(self):
        self.registerB = self.registerB ^ self.literal_operand
        self.instruction_pointer += 2

    def bst(self):
        self.registerB = self.combo_operand % 8
        self.instruction_pointer += 2

    def jnz(self):
        if self.registerA != 0:
            self.instruction_pointer = self.literal_operand
        else:
            self.instruction_pointer += 2

    def bxc(self):
        self.registerB = self.registerB ^ self.registerC
        self.instruction_pointer += 2

    def out(self):
        self.output.append(self.combo_operand % 8)
        self.instruction_pointer += 2

    def bdv(self):
        self.registerB = self.registerA // (2 ** (self.combo_operand))
        self.instruction_pointer += 2

    def cdv(self):
        self.registerC = self.registerA // (2 ** (self.combo_operand))
        self.instruction_pointer += 2

    def execute_program(self):
        while self.instruction_pointer < len(self.program) - 1:

            self.opcode = self.program[self.instruction_pointer]
            self.literal_operand = self.program[self.instruction_pointer + 1]
            self.set_combo_operand()

            if self.opcode == 0:
                self.adv()
            elif self.opcode == 1:
                self.bxl()
            elif self.opcode == 2:
                self.bst()
            elif self.opcode == 3:
                self.jnz()
            elif self.opcode == 4:
                self.bxc()
            elif self.opcode == 5:
                self.out()
            elif self.opcode == 6:
                self.bdv()
            elif self.opcode == 7:
                self.cdv()


"""
Unit Tests
"""


def test1():
    myComputer = Computer()
    myComputer.registerC = 9
    myComputer.program = np.array([2, 6])
    myComputer.opcode = myComputer.program[0]
    myComputer.literal_operand = myComputer.program[1]
    myComputer.execute_program()
    assert myComputer.registerB == 1


def test2():
    myComputer = Computer()
    myComputer.registerA = 10
    myComputer.program = np.array([5, 0, 5, 1, 5, 4])
    myComputer.opcode = myComputer.program[0]
    myComputer.literal_operand = myComputer.program[1]
    myComputer.set_combo_operand()
    myComputer.execute_program()
    assert (myComputer.output == np.array([0, 1, 2])).all()


def test3():
    myComputer = Computer()
    myComputer.registerA = 2024
    myComputer.program = np.array([0, 1, 5, 4, 3, 0])
    myComputer.opcode = myComputer.program[0]
    myComputer.literal_operand = myComputer.program[1]
    myComputer.set_combo_operand()
    myComputer.execute_program()
    assert (myComputer.output == np.array([4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0])).all()
    assert myComputer.registerA == 0


def test4():
    myComputer = Computer()
    myComputer.registerB = 29
    myComputer.program = np.array([1, 7])
    myComputer.opcode = myComputer.program[0]
    myComputer.literal_operand = myComputer.program[1]
    myComputer.set_combo_operand()
    myComputer.execute_program()
    assert myComputer.registerB == 26


def test5():
    myComputer = Computer()
    myComputer.registerB = 2024
    myComputer.registerC = 43690
    myComputer.program = np.array([4, 0])
    myComputer.opcode = myComputer.program[0]
    myComputer.literal_operand = myComputer.program[1]
    myComputer.set_combo_operand()
    myComputer.execute_program()
    assert myComputer.registerB == 44354


def test6():
    myComputer = Computer()
    myComputer.execute_program()
    assert (myComputer.output == np.array([4, 6, 3, 5, 6, 3, 5, 2, 1, 0])).all()


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()

    myComputer = Computer(file="input.txt")
    myComputer.execute_program()
    print(",".join(np.array(myComputer.output).astype(str)))
