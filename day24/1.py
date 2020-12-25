# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    lines = [l.strip() for l in input_file.read().splitlines()]

# print(lines)
# e, se, sw, w, nw, and ne

b =set()
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

    if (x,y,z) in b:
        b.remove((x,y,z))
    else:
        b.add((x,y,z))
print(len(b))