from copy import deepcopy

# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    lines = [list(l.strip()) for l in input_file.read().splitlines()]
    

# print(lines)

# l = [list()]

x = len(lines[0])
y = len(lines)

# print(x,y)

equilibrium = 0

while True:
    
    # print('='*80)
    # for r in range(y):
    #     # print(''.join(lines[r]))

    newl = deepcopy(lines)
    change = False
    for r in range(y):
        for c in range(x):
            occupied = 0
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    if not (dr == 0 and dc == 0):
                        rr = r+dr
                        cc = c+dc
                        while 0<=rr<y and 0<=cc<x and lines[rr][cc] == '.':
                            rr = rr+dr
                            cc = cc+dc
                        if 0<=rr<y and 0<=cc<x and lines[rr][cc] == '#':
                            occupied += 1 
            # print(r,c,occupied)

            if lines[r][c] == 'L':
                if occupied == 0:
                    newl[r][c] = '#'
                    change = True
            elif lines[r][c] == '#' and occupied >= 5:
                newl[r][c] = 'L'
                change = True
    
    if not change:
        break
    lines = deepcopy(newl)
    equilibrium += 1

print(equilibrium)

res = 0
for r in range(y):
    for c in range(x):
        if lines[r][c] == '#':
            res += 1

print(res)