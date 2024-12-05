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

line = f.readline()
while line:

    rules_satisfied = True

    page = line.split(",")
    line = f.readline()

    page_len = len(page)
    for i, num_i in enumerate(page):
        for j in range(i + 1, page_len):
            num_i = int(num_i)
            num_j = int(page[j])

            try:
                if num_j in rules_dict[num_i]:
                    rules_satisfied = False
                    break
            except KeyError:
                pass
    if rules_satisfied:
        middle_page_sum += int(page[len(page) // 2])

f.close()

print(middle_page_sum)
