with open('inputs/test.txt') as input_file:
# with open('inputs/1.txt') as input_file:
    lines = input_file.read().splitlines()

# print(lines)

x=0
y=0

trees = 0

grid = []
for line in lines:
    grid.append(list(line.strip()))

# print(grid, len(grid), grid[0][2], grid[1][0])
# go grid[y][x]

while y + 1 < len(grid):
    x += 3
    y += 1
    if grid[y][x%len(grid[y])]=='#':
        trees += 1

print('Part 1:', trees)