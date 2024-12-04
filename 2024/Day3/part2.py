sum = 0

# for each letter:
# if it's d, check if do. then check if do( or don't(
# if do is active:
#   if it's m, check if mul(


f = open("input.txt", "r")
input = f.read()

char_idx = 0
do = True


def check_do():
    """
    Check if the next characters are "do" or "don't" and update the "do" tracker
    accordingly
    """
    global do
    if char_idx + 4 < len(input):
        if input[char_idx : char_idx + 4] == "do()":
            do = True
            return
    if char_idx + 7 < len(input):
        if input[char_idx : char_idx + 7] == "don't()":
            do = False
            return


def get_mul_product():
    global do
    num1 = ""
    num2 = ""
    if char_idx + 4 < len(input):
        if input[char_idx : char_idx + 4] == "mul(":
            i = 4
            while input[char_idx + i] != ",":
                num1 += input[char_idx + i]
                i += 1
            while input[char_idx + i + 1] != ")":
                num2 += input[char_idx + i + 1]
                i += 1
            try:
                return int(num1) * int(num2)
            except ValueError:
                return 0
    return 0


while char_idx < len(input):
    check_do()
    if do:
        sum += get_mul_product()
    char_idx += 1


print(sum)
