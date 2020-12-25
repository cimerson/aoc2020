# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    lines = [l.strip() for l in input_file.read().splitlines()]

# print(lines)

black = set()
for line in lines:
    x,y,z = 0,0,0
    i = 0
    while line:
        if line.startswith('e'):
            x += 1
            y -= 1
            line = line[1:]
        elif line.startswith('se'):
            y -= 1
            z += 1
            line = line[2:]
        elif line.startswith('sw'):
            x -= 1
            z += 1
            line = line[2:]
        elif line.startswith('w'):
            x -= 1
            y += 1
            line = line[1:]
        elif line.startswith('nw'):
            z -= 1
            y += 1
            line = line[2:]
        elif line.startswith('ne'):
            x += 1
            z -= 1
            line = line[2:]
        else:
            assert False

    if (x,y,z) in black:
        black.remove((x,y,z))
    else:
        black.add((x,y,z))
print('Part 1:',len(black))

for _ in range(100):
    newblack = set()
    check = set()
    for (x,y,z) in black:
        check.add((x,y,z))
        for (dx,dy,dz) in [(1,-1,0),(0,-1,1),(-1,0,1),(-1,1,0),(0,1,-1),(1,0,-1)]:
            check.add((x+dx,y+dy,z+dz))

    for (x,y,z) in check:
        nbr = 0
        for (dx,dy,dz) in [(1,-1,0),(0,-1,1),(-1,0,1),(-1,1,0),(0,1,-1),(1,0,-1)]:
            if (x+dx,y+dy,z+dz) in black:
                nbr += 1
        if (x,y,z) in black and (nbr==1 or nbr==2):
            newblack.add((x,y,z))
        if (x,y,z) not in black and nbr==2:
            newblack.add((x,y,z))
    black = newblack
print('Part 2:',len(black))
