# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    lines = input_file.read().splitlines()

# print(lines)

p1 = None
p2 = None

ids = set()

lines.append('')
for line in lines:
    line = line.strip()
    # print(line)

    row = 0
    rowp = 64

    column = 0
    columnp = 4

    for char in line:
        if char == 'B':
            row += rowp
            rowp //= 2
        elif char == 'F':
            rowp //= 2

        if char == 'R':
            column += columnp
            columnp //= 2
        elif char == 'L':
            columnp //= 2

    seat = row*8+column
    # print(seat)
    ids.add(seat)
    # print(ids)
    if p1:
        p1 = max(p1, seat)
    else:
        p1 = seat

# print(ids)
for id in ids:
    if id+1 not in ids and id+2 in ids:
        assert p2 is None
        # print(id+1)
        p2 = id+1

print('Part 1:', p1)
print('Part 2:', p2)