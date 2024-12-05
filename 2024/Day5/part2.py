from functools import cmp_to_key

f = open("input.txt", "r")

rules_dict = {}
middle_page_sum = 0

line = f.readline()
while line != "\n":
    num1_str, num2_str = line.split("|")
    num1 = int(num1_str)
    num2 = int(num2_str)
    line = f.readline()

    try:
        rules_dict[num2].append(num1)
    except KeyError:
        rules_dict[num2] = [num1]


def compare_nums(num1, num2):
    """
    Comparison algorithm to use for sorting. Return:
      0 if num1 == num2
      1 if num1 > num2
      -1 if num1 < num2
    """
    try:
        if num1 in rules_dict[num2]:
            return -1
    except KeyError:
        pass
    try:
        if num2 in rules_dict[num1]:
            return 1
    except KeyError:
        return 0


def get_middle_num_of_sorted_page(page):
    sorted_page = sorted(page, key=cmp_to_key(compare_nums))
    return int(sorted_page[len(sorted_page) // 2])


line = f.readline()
while line:

    rules_satisfied = True

    page = line.split(",")
    page = list(map(int, page))
    line = f.readline()

    page_len = len(page)
    for i, num_i in enumerate(page):
        for j in range(i + 1, page_len):

            try:
                if page[j] in rules_dict[num_i]:
                    rules_satisfied = False
                    break
            except KeyError:
                pass

    if not rules_satisfied:

        middle_page_sum += get_middle_num_of_sorted_page(page)
f.close()

print(middle_page_sum)
