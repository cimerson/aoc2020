import string

# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    lines = input_file.read().splitlines()

# print(lines)

# p1 = sum_group len(union(answers))
# p2 = sum_group len(intersection(answers))
p1 = 0
p2 = 0

# For any yes the operation is union (|), set()
# For all yes the operation is intersection (&), set(alphabet)
any_yes = None
all_yes = None

alphabet = string.ascii_lowercase
# print(alphabet)

lines.append('')
for line in lines:
    line = line.strip()
    if not line:
        # print(yes)
        p1 += len(any_yes)
        p2 += len(all_yes)
        any_yes = set()
        all_yes = set(alphabet)
    else:
        if any_yes is None:
            any_yes = set(line)
        else:
            any_yes = any_yes | set(line)

        if all_yes is None:
            all_yes = set(line)
        else:
            all_yes = all_yes & set(line)

print('Part 1:', p1)
print('Part 2:', p2)