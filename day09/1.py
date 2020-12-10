from itertools import combinations

# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    # lines = input_file.read().splitlines()
    lines = list([int(line) for line in input_file.read().splitlines()])

# print(lines)

lines.append('')
# for i in range(5, len(lines)):
for i in range(25, len(lines)):
    ok = True
    # prev = lines[i-5:i]
    prev = lines[i-25:i]
    # assert len(prev) == 5
    assert len(prev) == 25
    for y,z in combinations(prev, 2):
        if y+z == lines[i]:
            # print(y,z)
            ok = False
    # print(lines[i], prev)
    if ok:
        print(lines[i])
        break