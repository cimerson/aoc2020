# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    lines = input_file.read().splitlines()

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

grid = []
for line in lines:
    grid.append(list(line.strip()))

ans = 1
for (dirX, dirY) in slopes:
    x = 0
    y = 0
    trees = 0
    while y + 1 < len(grid):
        x += dirX
        y += dirY
        if grid[y][x%len(grid[y])]=='#':
            trees += 1
    ans *= trees

print('Part 2:', ans)