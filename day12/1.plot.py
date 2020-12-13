import matplotlib.pyplot as plt
import numpy as np

with open('inputs/test.txt') as input_file:
# with open('inputs/1.txt') as input_file:
    lines = [l.strip() for l in input_file.read().splitlines()]

# print(lines)

dx = [0,1,0,-1]
dy = [1,0,-1,0]
x = 0
y = 0
direction = 1

xplot = [0]
yplot = [0]

for line in lines:
    instruction = line[0]
    units = int(line[1:])
    # print(instruction, units)
    if instruction == 'N':
        y += units
    elif instruction == 'S':
        y -= units
    elif instruction == 'E':
        x += units
    elif instruction == 'W':
        x -= units
    elif instruction == 'L':
        direction = (direction+3*(units//90))%4
    elif instruction == 'R':
        direction = (direction+1*(units//90))%4
    elif instruction == 'F':
        x += dx[direction]*units
        y += dy[direction]*units
    else:
        assert False
    print(line, instruction, units, x, y)
    xplot.append(x)
    yplot.append(y)

# print(xplot)
# print(yplot)
xpoints = np.array(xplot)
ypoints = np.array(yplot)
# plt.plot([0, x], [0, y], 'o')
plt.plot(xpoints, ypoints, 'o')
plt.plot(xpoints, ypoints)
plt.show()

print(abs(x)+abs(y))
