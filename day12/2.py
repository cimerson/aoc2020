with open('inputs/test.txt') as input_file:
# with open('inputs/1.txt') as input_file:
    lines = [l.strip() for l in input_file.read().splitlines()]

# print(lines)
wx = 10
wy = 1
dx = [0,1,0,-1]
dy = [1,0,-1,0]
x = 0
y = 0
direction = 1

for line in lines:
    instruction = line[0]
    units = int(line[1:])
    # print(instruction, units)
    if instruction == 'N':
        wy += units
    elif instruction == 'S':
        wy -= units
    elif instruction == 'E':
        wx += units
    elif instruction == 'W':
        wx -= units
    elif instruction == 'L':
        for _ in range(units//90):
            wx,wy = -wy,wx
    elif instruction == 'R':
        for _ in range(units//90):
            wx,wy = wy,-wx
    elif instruction == 'F':
        x += units*wx
        y += units*wy
    else:
        assert False
    print(line, instruction, units, x, y)

print(abs(x)+abs(y))