# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    lines = input_file.read().splitlines()

# print(lines)

p1 = 0

yes = set()

lines.append('')
for line in lines:
    line = line.strip()
    if not line:
        # print(yes)
        p1 += len(yes)
        yes = set()
    else:
        for char in line:
            yes.add(char)

print(p1)