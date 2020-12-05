# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    lines = input_file.read().splitlines()

# print(lines)

p1 = 0

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
            # print('r', row)
        rowp /= 2
        # print('rp', rowp)

        if char == 'R':
            column += columnp
            # print('c', column)
            columnp /= 2
            # print('cp', columnp)
        elif char == 'L':
            columnp /= 2

    seat = row*8+column
    # print(seat)
    p1 = max(p1, seat)

print(p1)