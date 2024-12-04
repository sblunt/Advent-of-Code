sum = 0

# super inefficient but whatever Python be Python-ing :)

f = open("input.txt", "r")
for line in f:
    split_line = line.split("mul(")
    for sub_line in split_line:
        nums_sepby_comma = sub_line.split(")")

        for entry in nums_sepby_comma:
            nums2multiply = entry.split(",")
            try:
                if len(nums2multiply) == 2:
                    sum += int(nums2multiply[0]) * int(nums2multiply[1])
            except ValueError:
                pass

print(sum)
