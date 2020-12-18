# with open('inputs/test.txt') as input_file:
with open('inputs/1.txt') as input_file:
    # lines = input_file.read().splitlines()
    lines = [l.strip() for l in input_file.read().splitlines()]

print(lines)

state = set()

for r,rl in enumerate(lines):
    for c,cl in enumerate(rl):
        if cl == '#':
            state.add((r,c,0,0))
# print(state)

for _ in range(6):
    newstate = set()
    for  x in range(-15,15):
        for y in range(-15,15):
            for z in range(-7,7):
                for w in range(-7,7):
                    near = 0
                    for dx in [-1,0,1]:
                        for dy in [-1,0,1]:
                            for dz in [-1,0,1]:
                                for dw in [-1,0,1]:
                                    if dx!=0 or dy!=0 or dz!=0 or dw!=0:
                                        if(x+dx, y+dy, z+dz,w+dw) in state:
                                            near += 1
                    if (x,y,z,w) not in state and near == 3:
                        newstate.add((x,y,z,w))
                    if (x,y,z,w) in state and near in [2,3]:
                        newstate.add((x,y,z,w))
    state = newstate
    # for (x,y,z) in state:
    #     print(x,y,z)

print(len(state))